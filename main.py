import praw
import time



# giving praw information for bot to run
reddit=praw.Reddit(
    user_agent="windows:EA01:v!.0 (by u/ErAk_v2",
    client_id="t-9I0fc6PR29wiAQJMph_A",
    client_secret="6Puid5geA15oA0WitPKPMNeVLjNJnQ",
    username="sussy_baka_69421",
    password="29121969"
)

f = open("text", mode = 'r+')                                            # a file where we store old comments to avoid commenting more than 1 times
f.seek(0)                                                                # resetting cursors position just in case

subreddit = reddit.subreddit("okbuddyretard")                            # subreddit where this bot will work

while True:                                                              # a constant loop in case there isnt enough new posts
    i = 1                                                                # for debugging
    isVisited = 0                                                        # where if the comment had been visited or not is stored
    visitedComments = f.readlines()
    visitedComments = {x.replace("\n", "") for x in visitedComments}     #removing the new line "\n" from the id
    for post in subreddit.top("day"):                          # checking new comments on the subreddit
       print("***new post***")                                           # these are for debugging. Nothing important
       print(i)
       i += 1

       for comment in post.comments:                                     # checking every comment on a post
            if hasattr(comment, "body"):                                 # if the comment has any content
                f.seek(0)
                visitedComments = f.readlines()
                visitedComments = {x.replace("\n", "") for x in visitedComments}                             #removing the new line "\n" from the id
                for word in visitedComments:                             # checking the txt file for the same comment id
                    if comment.id == word:
                        #print("lol")
                        isVisited = 1                                    # if there is a same comment it will pass the if-else conditions
                comment_lower = comment.body.lower()                                                         # making the comment all lowercase.
                if isVisited == 0 and "sus" in comment_lower:                                                # if it finds "xxx" in the comment.
                    print("!!!sus dedected!!! " + comment.id + " " + post.title.lower() + " " + post.id)     # again for debugging.
                    print(comment_lower)
                    comment.reply("amogus")                                                                  # actually replying to the comment.
                    time.sleep(660)                                                                          # to avoid getting ratelimit error
                    f.writelines("\n" + comment.id)
                elif isVisited == 0 and "amogus" in comment_lower:  goog                                         # same as the above
                    print("!!!sus dedected!!! " + comment.id + " " + post.title.lower() + " " + post.id)
                    print(comment_lower)
                    comment.reply("sus")
                    time.sleep(660)
                    f.writelines("\n" + comment.id)
                isVisited = 0