import bs4, gtts

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    rticles = soup.find_all('article')  
    stories = []
    
    for article in articles:
        title = article.find('h2')  
        teaser = article.find('p')  
        
        title_text = title.get_text(strip=True) if title else ''
        teaser_text = teaser.get_text(strip=True) if teaser else ''
        
        stories.append((title_text, teaser_text))
    return stories
    
def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    if n < 0 or n >= len(stories):
        raise ValueError("Index out of range")
    
    title, teaser = stories[n]
    text_to_read = f"Title: {title}. Teaser: {teaser}" if teaser else f"Title: {title}."
    
   
    tts = gTTS(text=text_to_read, lang='en')
    tts.save(solution.mp3)
