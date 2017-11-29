import pandas as pd
df=pd.read_csv("election_data_1.csv") 
ed=pd.read_csv("election_data_2.csv")
frame = [df,ed]
election_result = pd.concat(frame)
#determines total votes and votes per candidate
total_votes = election_result.shape[0]
election_result.groupby(["Candidate"]).size()
candidate_count= election_result.groupby(["Candidate"]).size()
#deterimines winner
winner = candidate_count.idxmax()
#determines percent of total votes per candidate 
candidate_percent = round(candidate_count/total_votes * 100, 0)
#converts the float into a string and adds a percentage sign 
candidate_percent=candidate_percent.astype(str)
for i in range(len(candidate_percent)):
    candidate_percent[i]=candidate_percent[i]+"%" 
with open('result.txt','w') as f:  
    print("Election Results\n---------------------\n"+str(total_votes)+"\n---------------------\n"+str(candidate_percent)+"\n---------------------\n"+str(winner)+"\n---------------------\n", file=f)
    




