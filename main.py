insta_data=[
2                {
3                 'name':'Justin bieber' ,
4                 'followers':50 ,
5                 'profession':'Artist'
6                 },
7                 {
8                  'name':'Justin Timberlake' , 
9                  'followers':70 ,
10                  'profession':'Artist'
11                  }
12                ]   
13    def compare_followers(guess,a_followers,b_followers):
14        if a_followers>b_followers:
15            return guess=="a" 
16        else:
17            return guess=="b" 
18            
19    a_follower= insta_data[0] 
20    b_follower=insta_data[1] 
      a_followers=a_follower["followers"]
      b_followers=b_follower["followers"] 
      guess=input("Guess 'A' or 'B').lower() 
     compare_followers(guess,a_followers,b_followers)  