def text_from_path(path):
    with open(path) as f:
       file_content=f.read()
       words = file_content.split()
       return words




def count(words,text):
   result=0
   for word in words:
      lowered_string=word.lower()
      if lowered_string==text:
         result+=1
   return result



def main():
   text_list= text_from_path("books/frankenstein.txt")
   print(count(text_list, "including"))
main()