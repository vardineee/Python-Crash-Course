def show_messages(text_messages):
    for text_message in text_messages:
        print(text_message.title())
    
def send_messages(sent_messages):
    while text_messages:
        current_message = text_messages.pop()
        print(current_message)
        sent_messages.append(current_message)
        


text_messages =['hello', 'welcome', 'bye']
show_messages(text_messages)
sent_messages =[]
send_messages(sent_messages)

print('Final list')
print(text_messages)
print(sent_messages)

    