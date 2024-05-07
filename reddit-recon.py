#!/usr/bin/python

from src.scrapers.reddit_user_activity_scraper import RedditUserActivityScraper
from src.scrapers.subreddit_scraper import SubredditScraper
from src.scrapers.subreddit_user_activity_scraper import SubredditUserActivityScraper
from src.scrapers.subreddit_search_scraper import SubredditSearchScraper


def main(): 
    print(
        '''                                                   

                                      
   ██████╗ ███████╗██████╗ ██████╗ ██╗████████╗   
   ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝   
   ██████╔╝█████╗  ██║  ██║██║  ██║██║   ██║ 
   ██║  ██║███████╗██████╔╝██████╔╝██║   ██║      
   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚═╝   ╚═╝      
  
            ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
            ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
            ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
            ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
            ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ v0.1                                                                                                                                                                             
      ╔══════════════════════════════════════════════╗
      ║                                              ║
      ║    ᴄʜᴏᴏsᴇ ғʀᴏᴍ ᴛʜᴇ ᴏᴘᴛɪᴏɴs ʙᴇʟᴏᴡ:            ║
      ║                                              ║
      ║    ᴅᴀᴛᴀᴍɪɴɪɴɢ:                               ║
      ║                                              ║
      ║     [1] Sᴄʀᴀᴘᴇ ᴀ Sᴜʙʀᴇᴅᴅɪᴛ                   ║
      ║     [2] Sᴇᴀʀᴄʜ & Sᴄʀᴀᴘᴇ ᴀ Sᴜʙʀᴇᴅᴅɪᴛ          ║
      ║     [3] Sᴄʀᴀᴘᴇ Sᴜʙʀᴇᴅᴅɪᴛ Usᴇʀ Aᴄᴛɪᴠɪᴛʏ       ║
      ║     [4] Sᴄʀᴀᴘᴇ Rᴇᴅᴅɪᴛ Usᴇʀ Aᴄᴛɪᴠɪᴛʏ          ║
      ║                                              ║
      ║     [exit] ᴏ̨ᴜɪᴛ ᴛʜᴇ ᴀᴘᴘʟɪᴄᴀᴛɪᴏɴ              ║
      ║                                              ║
      ╚══════════════════════════════════════════════╝
        
        '''
    )
    
    while True: 
        user_input = input("\nᴇɴᴛᴇʀ ᴀ ᴄᴏᴍᴍᴀɴᴅ (1, 2, 3, 4 ᴏʀ 'ᴇxɪᴛ' ᴛᴏ ǫᴜɪᴛ): ")
        
        if user_input == '1':
            print("\nYou selected option 1: 'Scrape a Subreddit.'\n")
            subreddit_names = input("Enter one or more Subreddit Names [e.g., datascience MachineLearning]: ")
            category_name = input("\nEnter an output directory name: ")
            post_type = input("\nSelect a post type - new, top, or hot: ")
            subreddit_names = subreddit_names.split(' ')
            
            scraper = SubredditScraper(subreddits=subreddit_names, category=category_name)
            scraper.extract_subreddit_data(post_type=post_type)
        
        elif user_input == '2':
            print("\nYou selected option 2: 'Search & Scrape a Subreddit.'\n")
            subreddit_names = input("Enter one or more Subreddit Names [e.g., datascience MachineLearning]: ")
            search_query_items = input("\nEnter one or more Search Query Items [e.g., AGI GPT]: ")
            category_name = input("\nEnter an output directory name: ")
            post_type = input("\nSelect a post type [e.g., new, top, hot]: ")
            subreddit_names = subreddit_names.split(' ')
            search_query_items = search_query_items.split(' ')
            
            scraper = SubredditSearchScraper(subreddits=subreddit_names, category=category_name)
            scraper.extract_search_subreddit_data(search_query_items=search_query_items, post_type=post_type)
            
        elif user_input == '3':
            print("\nYou selected option 3: 'Scrape Subreddit User Activity.'\n")
            subreddit_names = input("Enter one or more Subreddit Names [e.g., datascience MachineLearning]: ")
            category_name = input("\nEnter an output directory name: ")
            subreddit_names = subreddit_names.split(' ')

            scraper = SubredditUserActivityScraper(subreddits=subreddit_names, category=category_name)
            scraper.extract_subreddit_user_activity()
            
        elif user_input == '4':
            print("\nYou selected option 4: 'Scrape Reddit User Activity.'\n")
            usernames = input("Enter one or more Reddit Usernames [e.g., <username> <username>]: ")
            post_type = input("\nSelect a post type [e.g., new, top, hot]: ")
            usernames = usernames.split(' ')

            scraper = RedditUserActivityScraper(post_type=post_type)
            scraper.extract_user_activity(usernames=usernames)
        
        elif user_input.lower() in ['exit', 'quit', 'q']:
            print(
                '''\n\n\n  
                       ＧＯＯＤＢＹＥ！       
                       
        _    .  ,   .            .
    *  / \_ *  / \_      _  *        *   /\'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \ 
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._ Ⓚ
                                     

                  ''')
            break 
        
        else:
            print("\nSelection Invalid. Please try again.\n")




if __name__ == "__main__":
    main()
