from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output



def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    
    return word in text



# Creating a bubble sort function  
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
    


