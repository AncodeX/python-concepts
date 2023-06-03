"""
Lee esta url y encuentra las 10 palabras más frecuentes. 

    romeo_y_julieta = ' http://www.gutenberg.org/files/1112/1112.txt '
"""
import requests, string


def main(nw):
    response = requests.get("https://www.gutenberg.org/files/1112/1112.txt")
    
    content = response.text.lower()
    punctuation = string.punctuation

    for p in punctuation:
        content = content.replace(p, "")
    
    frequent_words = {}
    words = content.split()

    for word in words:
        if word in frequent_words:
            frequent_words[word] += 1
        else:
            frequent_words[word] = 1

    sorted_words = sorted(frequent_words.items(), key=lambda x: x[1], reverse=True)

    return sorted_words[:nw]
    


if __name__ == "__main__":
    print(main(12))