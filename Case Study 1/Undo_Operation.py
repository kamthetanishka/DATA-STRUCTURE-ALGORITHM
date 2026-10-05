class Operation:
    def __init__(self):
        self.action = -1
        self.undo = [0]* 25
    def Perform_action(self,x):
        if self.action ==24:
            print("Undo stack is full....... Cannot perform new action.....")
            return
        self.action = self.action +1
        self.undo[self.action] = x
    def Undo_action(self):    
        if self.action == -1:
            print("No previous action to undo......")
        else:
            print("Undoing action:", self.undo[self.action])
            self.action = self.action - 1
    def Current_action(self):
        if self.action == -1:
            print("No current action.")
        else:
            print("Current Action:", self.undo[self.action])
            self.action = self.action - 1   
    def Display_action(self):
        if self.action == -1:
            print("Undo stack is empty.")
        else:
            print("\nUndo Stack (Latest to Oldest):")
            for i in range(self.action, -1, -1):
                print(self.undo[i])
                
o =Operation()
while True:
    c = input("\n===== Undo Operation Menu =====\n1. Perform New Action\n2. Undo Last Action\n3. Current Action\n4. Display Undo Stack\n5. Exit\nEnter your choice: ")
    if c == "1":
        x = input("Enter the action to be performed:") 
        o.Perform_action(x)
    elif c == "2":
        o.Undo_action() 
    elif c == "3":
        o.Current_action()
    elif c == "4":
        o.Display_action() 
    elif c == "5":
        print("Exiting...")
        break                
                                