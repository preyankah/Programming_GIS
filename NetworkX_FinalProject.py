__author__ = 'priyankaverma'


import tweepy
import time
import networkx as nx
import matplotlib.pyplot as plt



#credentials
consumer_key =''
consumer_secret=''
access_token=''
access_secret=''


'''Function Definitions'''
#Function uses credentials defined to connect to twitter
def SignInToTwitter(consumer_key,consumer_secret,access_token,access_secret):
    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    global api
    api = tweepy.API(auth) #API object with Authentication
    if(api.verify_credentials):
        print ('Authorized & Successfully Logged in')


#Uses twitter function "friends" to get userids of friends
def GetFriends(file,screen_name):
    user = tweepy.Cursor(api.friends, screen_name=screen_name).items()
    print("Printing Friends -- Start Time: " + time.strftime('%c'))
    while True:
        try:
            for u in user:
                u = next(user)
                file.write(u.screen_name +' \n')
                print(u.screen_name)
        except:
            print ('Pause-- Requests halted. Program will sleep for 15 Mins to avoid hitting limit')
            time.sleep(900)
            print ('Rate Restored. Try next user')
            break
        file.close()
        break
    print("Returned -- End Time: " + time.strftime('%c'))


#Converts the response from Twitter written to text file from last function to a list
def TxtToList(txtfile, list):
    f = open(txtfile)
    for user in f:
        user=user.strip('\n')
        list.append(user)


#checks if source follows target
def CheckFriendship(source,targetls,followlist):
    for t in targetls:
        target = t
        user = api.show_friendship(source_screen_name=source,target_screen_name=target)
        a = str(user[0])#returns relationship of source to target
        #print(a)
        if "following=True" in a:
            print('Source follows target')
            followlist.append(t)
        else:
            pass
            print('Source does not follow target user')
    print("followlist:", followlist)


#Add nodes for every single user connected
def add_NodesEdges(list,source):
    for i in (list):
        G.add_node(i)
        G.add_edge(i,source,weight=0.6)


#edges for connections between users
def add_Connections(list,source):
    for i in (list):
        G.add_edge(i,source,weight=2)


if __name__ == '__main__':

    #Three main twitter accounts
    user1 = 'POTUS'
    user2 = 'FLOTUS'
    user3 = 'VP'

    '''INITIALIZE LISTS'''
    u1_friends = []
    u2_friends = []
    u3_friends = []
    newlist1 = ["POTUS"]
    newlist2 = ["FLOTUS"]
    newlist3 = ["VP"]


    '''FUNCTION CALLS'''
    #specify file to write results to
    list1= open(r'friendlist1.txt','w')
    list2 = open(r'friendlist2.txt','w')
    list3 = open(r'friendlist3.txt','w')

    SignInToTwitter(consumer_key,consumer_secret,access_token,access_secret)

    GetFriends(list1,"POTUS")
    GetFriends(list2,"FLOTUS")
    GetFriends(list3,"VP")

    list1.close()
    list2.close()
    list3.close()

    TxtToList("friendlist1.txt",u1_friends)
    TxtToList("friendlist2.txt",u2_friends)
    TxtToList("friendlist3.txt",u3_friends)

    CheckFriendship("FLOTUS",u1_friends,newlist1)
    CheckFriendship("VP",u2_friends,newlist2)
    CheckFriendship("POTUS",u3_friends,newlist3)



    ''' NETWORKX GRAPH'''

    G=nx.Graph()

    #nodes for all users being followed by a user with source
    add_NodesEdges(u1_friends,user1)
    add_NodesEdges(u2_friends,user2)
    add_NodesEdges(u3_friends,user3)

    #nodes for mutual connections
    add_Connections(newlist1,user2)
    add_Connections(newlist2,user3)
    add_Connections(newlist3,user1)

    #nodes to identify common users to all
    common = []
    for node in G.nodes():
            if (node in newlist1) and (node in newlist2) and (node in newlist3):
                common.append(node)
                #print(node)

    #list of 3 main users
    slist = []
    slist.append(user1)
    slist.append(user2)
    slist.append(user3)

    #convert list of main users to dictionary for label creation
    friendlist = {}
    for x in slist:
        friendlist[x] = x


    pos = nx.spring_layout(G)

    #nodes for all friends
    nx.draw_networkx_nodes(G,pos,u1_friends,node_color='burlywood', with_labels=False,node_size=18,alpha=0.7,node_shape='s')
    nx.draw_networkx_nodes(G,pos,u2_friends,node_color='tan', with_labels=False,node_size=18,alpha=0.7,node_shape='s')
    nx.draw_networkx_nodes(G,pos,u3_friends,node_color='sandybrown', with_labels=False,node_size=18,alpha=0.7,node_shape='s')

    #nodes for connections
    nx.draw_networkx_nodes(G,pos,newlist1,node_color='brown',node_size=50,label='Between POTUS & FLOTUS')
    nx.draw_networkx_nodes(G,pos,newlist2,node_color='green', node_size=50,label='Between FLOTUS & VP')
    nx.draw_networkx_nodes(G,pos,newlist3,node_color='orange',node_size=50,label='Between VP & POTUS')

    #nodes for main users and all shared connections
    nx.draw_networkx_nodes(G,pos,slist,node_color='midnightblue', with_labels=True,node_size=1000,alpha=0.9)
    nx.draw_networkx_nodes(G,pos,common,node_color='springgreen', with_labels=False,node_size=200, label = 'Shared Between All')
    nx.draw_networkx_labels(G,pos,friendlist,font_size=8,font_family = 'f',font_color='ivory')


    #draw and style edge based on weight
    connectionedge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] > 1]
    normaledge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <= 0.7]
    nx.draw_networkx_edges(G,pos,edgelist=connectionedge,width=2,edge_color='red')
    nx.draw_networkx_edges(G,pos,edgelist=normaledge,width=.6,alpha=0.7,edge_color='grey',style='dashed')


    plt.legend(scatterpoints=1,loc=0, fancybox=True,labelspacing=1,shadow=True,fontsize=10)
    plt.axis('on')
    plt.tick_params(axis= 'x',which='both',bottom='off',top='off',labelbottom='off')
    plt.tick_params(axis= 'y',which='both',right='off',left='off',labelleft='off')
    plt.title('Mutual Friend Connections Between Twitter Accounts: '+ user1 + " & " + user2 + " & " + user3)

    #plt.savefig("networkx.png")
    plt.show()



