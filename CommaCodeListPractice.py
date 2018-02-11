import copy

def Comma(List):
    Text=''
    for i in range(len(List)-1):
        Text=Text+List[i]+', '
    Text=Text+' and '+List[-1]
    print(Text)
    return Text


spam=['apples','bananas','tofu','cats']
press=Comma(spam)