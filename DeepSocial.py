import requests
import argparse

def exibir_ascii_art():
    ascii_art = '''
    \033[35m7MM"""Yb.\033[0m                                 .M"""bgd                      db           `7MM
    \033[35m  MM    `Yb.\033[0m                              ,MI    "Y                                     MM
    \033[35m  MM     `Mb  .gP"Ya   .gP"Ya  `7MMpdMAo.\033[0m `MMb.      ,pW"Wq.   ,p6"bo  `7MM   ,6"Yb.    MM
    \033[35m  MM      MM ,M'   Yb ,M'   Yb   MM   `Wb\033[0m   `YMMNq. 6W'   `Wb 6M'  OO    MM  8)   MM    MM
    \033[35m  MM     ,MP 8M"""""" 8M""""""   MM    M8\033[0m .     `MM 8M     M8 8M         MM   ,pm9MM    MM
    \033[35m  MM    ,dP' YM.    , YM.    ,   MM   ,AP\033[0m Mb     dM YA.   ,A9 YM.    ,   MM  8M   MM    MM
    \033[35m.JMMmmmdP'    `Mbmmd'  `Mbmmd'   MMbmmd' \033[0m P"Ybmmd"   `Ybmd9'   YMbmd'  .JMML.`Moo9^Yo..JMML.
    \033[35m                                 MM\033[0m             
    \033[35m                               .JMML.\033[0m                 
        
    \033[33m                          Social Media Researcher Profile Tool\033[0m
    \033[90m                                  [+] git @sous4sec\033[0m
    '''
    print(ascii_art)

COLORS = {
    "dark_purple": "\033[38;5;55m",
    "light_purple": "\033[38;5;141m",
    "gray_purple": "\033[38;5;60m",
    "purple": "\033[38;5;129m",
    "light_gray": "\033[38;5;244m",
    "cyan": "\033[38;5;51m",
    "soft_yellow": "\033[38;5;190m",
    "soft_blue": "\033[38;5;68m",
    "soft_green": "\033[38;5;34m",
    "soft_red": "\033[38;5;160m",
    "reset": "\033[0m",
    "bold": "\033[1m",
}

def check_user(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if "page not found" in response.text.lower():
                return "red"
            else:
                return "green"
        else:
            return "red"
    except requests.exceptions.RequestException:
        return "red"

def search_user(username, specific_categories=None):
    platforms = {
        "Social Media": {
            "Twitter": f"https://x.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "Instagram": f"https://www.instagram.com/{username}",
            "Threads": f"https://www.threads.net/@{username}",
            "Facebook": f"https://www.facebook.com/{username}",
            "Telegram": f"https://t.me/{username}",
            "YouTube (Channel)": f"https://www.youtube.com/c/{username}",
            "YouTube (User)": f"https://www.youtube.com/@{username}",
            "TikTok": f"https://www.tiktok.com/@{username}",
            "Pinterest": f"https://www.pinterest.com/{username}",
            "Snapchat": f"https://www.snapchat.com/add/{username}",
            "Vero": f"https://www.vero.co/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "Tumblr": f"https://{username}.tumblr.com",
            "Flickr": f"https://www.flickr.com/photos/{username}",
            "Periscope": f"https://www.pscp.tv/{username}",
            "Clubhouse": f"https://www.joinclubhouse.com/{username}",
            "Mastodon": f"https://mastodon.social/@{username}",
            "Bumble": f"https://bumble.com/user/{username}",
            "Discord": f"https://discordapp.com/users/{username}",
        },
        "Shops": {
            "eBay": f"https://www.ebay.com/usr/{username}",
            "Amazon": f"https://www.amazon.com/author/{username}",
            "Etsy": f"https://www.etsy.com/shop/{username}",
            "Alibaba": f"https://{username}.en.alibaba.com",
            "MercadoLibre": f"https://www.mercadolivre.com.br/u/{username}",
            "Walmart": f"https://www.walmart.com/search/?query={username}",
            "Best Buy": f"https://www.bestbuy.com/site/searchpage.jsp?st={username}",
            "Target": f"https://www.target.com/s?searchTerm={username}",
            "Rakuten": f"https://www.rakuten.com/shop/{username}",
            "Newegg": f"https://www.newegg.com/p/pla-{username}",
            "Shopify": f"https://{username}.myshopify.com",
            "Zalando": f"https://www.zalando.com/{username}",
            "Wayfair": f"https://www.wayfair.com/brand/{username}",
            "Overstock": f"https://www.overstock.com/author/{username}",
            "AliExpress": f"https://www.aliexpress.com/store/{username}",
            "Flipkart": f"https://www.flipkart.com/shop/{username}",
            "B&H": f"https://www.bhphotovideo.com/c/search/{username}",
            "JD.com": f"https://www.jd.com/user/{username}",
            "Shopee": f"https://shopee.com/{username}",
        },
        "Hack Sites": {
            "Hack The Box": f"https://www.hackthebox.eu/profile/{username}",
            "TryHackMe": f"https://tryhackme.com/p/{username}",
            "VulnHub": f"https://vulnhub.com/user/{username}",
            "HackThisSite": f"https://www.hackthissite.org/user/{username}",
            "Root Me": f"https://www.root-me.org/?page=user&id={username}",
            "PentesterLab": f"https://www.pentesterlab.com/users/{username}",
            "CTFtime": f"https://ctftime.org/team/{username}",
            "Offensive Security": f"https://www.offensive-security.com/user/{username}",
            "Security Boulevard": f"https://www.securityboulevard.com/author/{username}",
            "Exploit-DB": f"https://www.exploit-db.com/user/{username}",
        },
        "Work Platforms": {
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "Upwork": f"https://www.upwork.com/freelancers/~{username}",
            "Fiverr": f"https://www.fiverr.com/{username}",
            "Trello": f"https://trello.com/{username}",
            "Freelancer": f"https://www.freelancer.com/u/{username}",
            "Guru": f"https://www.guru.com/freelancers/{username}",
            "PeoplePerHour": f"https://www.peopleperhour.com/freelancer/{username}",
            "WeWorkRemotely": f"https://weworkremotely.com/remote-jobs/{username}",
            "Hubstaff Talent": f"https://talent.hubstaff.com/companies/{username}",
            "AngelList": f"https://angel.co/people/{username}",
        },
        "Streaming Platforms": {
            "Spotify": f"https://open.spotify.com/user/{username}",
            "SoundCloud": f"https://soundcloud.com/{username}",
            "Apple Music": f"https://music.apple.com/us/profile/{username}",
            "Tidal": f"https://tidal.com/browse/artist/{username}",
            "Pandora": f"https://www.pandora.com/profile/{username}",
            "Deezer": f"https://www.deezer.com/us/profile/{username}",
            "Bandcamp": f"https://{username}.bandcamp.com",
            "YouTube Music": f"https://music.youtube.com/channel/{username}",
            "Napster": f"https://us.napster.com/user/{username}",
            "Vimeo": f"https://vimeo.com/{username}",
            "Dailymotion": f"https://www.dailymotion.com/{username}",
            "Mixcloud": f"https://www.mixcloud.com/{username}",
            "TuneIn": f"https://tunein.com/radio/{username}",
            "Stitcher": f"https://www.stitcher.com/user/{username}",
            "Rhapsody": f"https://www.rhapsody.com/artist/{username}",
            "SoundClick": f"https://www.soundclick.com/{username}",
            "SiriusXM": f"https://www.siriusxm.com/{username}",
            "iHeartRadio": f"https://www.iheart.com/podcast/{username}",
            "MySpace": f"https://myspace.com/{username}",
        },
    }

    if specific_categories:
        categories = {key: platforms[key] for key in specific_categories if key in platforms}
    else:
        categories = platforms

    print(f"\n{COLORS['light_gray']}[>] User Search:{COLORS['reset']} {COLORS['soft_yellow']}{username}{COLORS['reset']}")

    profiles_found = 0
    profiles_not_found = 0
    profiles_uncertain = 0
    total_profiles = 0

    for category, platforms_category in categories.items():
        print(f"\n{COLORS['light_purple']}[~] Category:{COLORS['reset']} {COLORS['soft_blue']}{category}{COLORS['reset']}:")
        for platform, link in platforms_category.items():
            result = check_user(link)
            total_profiles += 1

            if result == "green":
                print(f"  {COLORS['soft_green']}[+]{COLORS['reset']} {COLORS['light_gray']}{platform}{COLORS['reset']}: {COLORS['reset']}{link}{COLORS['reset']}")
                profiles_found += 1
            elif result == "red":
                print(f"  {COLORS['soft_red']}[-]{COLORS['reset']} {COLORS['light_gray']}{platform}{COLORS['reset']}: {COLORS['soft_red']}{link}{COLORS['reset']}")
                profiles_not_found += 1
            else:
                print(f"  {COLORS['soft_yellow']}[~]{COLORS['reset']} {COLORS['light_gray']}{platform}{COLORS['reset']}: {COLORS['soft_yellow']}{link}{COLORS['reset']}")
                profiles_uncertain += 1

    print(f"\n{COLORS['purple']}[/] Search Summary:{COLORS['reset']}\n")
    print(f"  {COLORS['soft_green']}[+]{COLORS['reset']} {profiles_found} profiles found")
    print(f"  {COLORS['soft_yellow']}[~]{COLORS['reset']} {profiles_uncertain} uncertain profiles")
    print(f"  {COLORS['soft_red']}[-]{COLORS['reset']} {profiles_not_found} profiles not found")
    print(f"  \n{COLORS['light_gray']}[i] Total profiles searched: {COLORS['reset']}{total_profiles}")

def process_arguments():
    parser = argparse.ArgumentParser(
        description="Search for users across various platforms."
    )

    parser.add_argument(
        'username', 
        nargs='?',
        help="[i] The username to search for (e.g., 'john_doe'). This is the identifier used across different platforms."
    )
    
    parser.add_argument(
        '--c', 
        choices=['all', 'sm', 's', 'w', 'st', 'ht'], 
        default='all', 
        help=( 
            "[=] Categories to search in. Choose one or more of the following:\n"
            "  [all]   - Search across all categories: Social Media, Shops, Work Platforms, Streaming Platforms (default).\n"
            "  [sm]    - Search only in Social Media platforms (Twitter, Instagram, LinkedIn, etc.).\n"
            "  [s]     - Search only in Shops (e.g., eBay, Amazon, Etsy).\n"
            "  [w]     - Search only in Work Platforms (e.g., LinkedIn, Upwork, Freelancer).\n"
            "  [st]    - Search only in Streaming Platforms (e.g., Spotify, YouTube, SoundCloud).\n"
            "  [ht]    - Search only in Hack sites (e.g., HackTheBox, TryHackMe, VulnHub)."
        )
    )

    args = parser.parse_args()
    
    if not args.username:
        print(f"\nError: The following arguments are required: username\n")
        print(f"Usage: DeepSocial.py [-h] [--c {{all,sm,s,w,st,ht}}] username\n")
        print(f"Use '--help' for more information.")
        exit()

    category_map = {
        'sm': ['Social Media'],
        's': ['Shops'],
        'w': ['Work Platforms'],
        'st': ['Streaming Platforms'],
        'ht': ['Hack Sites'],
        'all': ['Social Media', 'Shops', 'Work Platforms', 'Streaming Platforms', 'Hack Sites']
    }

    categories = category_map.get(args.c, ['Social Media', 'Shops', 'Work Platforms', 'Streaming Platforms'])

    return args.username, categories

def main():
    exibir_ascii_art()
    username, categories = process_arguments()
    search_user(username, categories)

if __name__ == "__main__":
    main()
