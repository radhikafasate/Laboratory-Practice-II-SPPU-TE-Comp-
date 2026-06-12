pairs = {
    "hello":            "Hello! Welcome to QuickShop. How can I help you?",
    "hi":               "Hi there! How can I assist you today?",
    "order":            "To track your order, visit My Orders section on our website.",
    "track":            "You can track your order using the tracking ID sent to your email.",
    "return":           "We have a 30-day return policy. Visit My Orders to initiate return.",
    "refund":           "Refunds are processed within 5-7 business days.",
    "payment":          "We accept Credit Card, Debit Card, UPI and Net Banking.",
    "delivery":         "Standard delivery takes 3-5 business days. Free delivery above Rs.499.",
    "discount":         "Use code FIRST10 for 10% off on your first order!",
    "offer":            "Check our Offers page for latest deals and discounts.",
    "cancel":           "You can cancel your order within 24 hours from My Orders section.",
    "contact":          "Call us at 1800-123-4567 or email support@quickshop.com",
    "help":             "I can help with orders, returns, payments, delivery and offers.",
    "thank you":        "You're welcome! Is there anything else I can help you with?",
    "thanks":           "Happy to help! Let me know if you need anything else.",
    "bye":              "Goodbye! Thank you for visiting QuickShop. Have a great day!",
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in pairs:
        if key in user_input:
            return pairs[key]
    return "I'm sorry, I didn't understand. Please call 1800-123-4567 for help."

def main():
    print("================================")
    print("   QuickShop Customer Chatbot")
    print("================================")
    print("Bot: Hello! How can I help you? (type 'bye' to exit)\n")

    while True:
        user = input("You: ").strip()
        if not user:
            continue
        response = get_response(user)
        print(f"Bot: {response}\n")
        if "bye" in user.lower():
            break

main()