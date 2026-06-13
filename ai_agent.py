import time

class NayePankhAIAgent:
    def __init__(self):
        # Agent Memory: Yeh user ke naam aur pichli baaton ko yaad rakhega
        self.memory = {
            "user_name": None,
            "interaction_history": []
        }
        self.agent_name = "Pankh-Bot 1.0"
        
    def greet_user(self):
        print(f"[{self.agent_name}]: Hello! I am an automated AI Agent for NayePankh Foundation.")
        if not self.memory["user_name"]:
            name = input(f"[{self.agent_name}]: May I know your name first? \n>> User: ")
            self.memory["user_name"] = name
            print(f"[{self.agent_name}]: Welcome {name}! How can NayePankh AI Agent assist you today?")
            
    def process_task(self, user_intent):
        # Memory Update
        self.memory["interaction_history"].append(user_intent)
        print(f"\n[AI Agent Thinking...] Analyzing intent and accessing memory...")
        time.sleep(1) # Simulation of thinking
        
        query = user_intent.lower()
        
        # Automation & Classification Logic (Decision Making)
        if "donate" in query or "money" in query or "funds" in query:
            return self.execute_finance_workflow()
        elif "volunteer" in query or "join" in query or "work" in query:
            return self.execute_volunteer_workflow()
        elif "history" in query or "memory" in query:
            return self.show_agent_memory()
        elif "exit" in query or "bye" in query:
            return "EXIT"
        else:
            return f"[{self.agent_name}]: Task unclassified. Routing this query to a human administrator for review."

    def execute_finance_workflow(self):
        # Automated workflow for donation routing
        return (f"🤖 [Workflow Triggered: Finance Automation System]\n"
                f"-> Generating secure payment link...\n"
                f"-> Action: Notification sent to Finance Team.\n"
                f"-> Response: '{self.memory['user_name']}, thank you! Your intent has been logged for donation tracking.'")

    def execute_volunteer_workflow(self):
        # Automated workflow for volunteer registration
        return (f"🤖 [Workflow Triggered: HR & Volunteer Allocation System]\n"
                f"-> Opening Volunteer Database...\n"
                f"-> Action: Matching user skills with current NGO requirements.\n"
                f"-> Response: 'Great choice, {self.memory['user_name']}! Our team will contact you shortly for onboarding.'")

    def show_agent_memory(self):
        # Accessing Agent's short-term memory
        history = ", ".join(self.memory["interaction_history"][:-1]) if len(self.memory["interaction_history"]) > 1 else "None"
        return (f"🧠 [Agent Memory Access]\n"
                f"-> User Identified: {self.memory['user_name']}\n"
                f"-> Past Queries Remembered: [{history}]\n"
                f"-> Status: Memory Active & Tracking Context.")

# Main Agent Execution Loop
if __name__ == "__main__":
    agent = NayePankhAIAgent()
    agent.greet_user()
    
    while True:
        user_input = input(f"\n>> {agent.memory['user_name']}: ")
        result = agent.process_task(user_input)
        
        if result == "EXIT":
            print(f"[{agent.agent_name}]: Goodbye {agent.memory['user_name']}! Memory cleared. Have a great day!")
            break
        else:
            print(result)
