def categorize_age(age):
    if age < 0:
        return "Invalid"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 35:
        return "Young Adult"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior Citizen"


def hobby_response(hobby):
    hobby = hobby.lower()

    if hobby in ["coding", "programming", "tech"]:
        return "💻 That's amazing! Technology skills are powerful for the future."
    elif hobby in ["sports", "cricket", "football", "badminton"]:
        return "🏆 Great! Sports keep you active and disciplined."
    elif hobby in ["music", "singing", "dance"]:
        return "🎵 Wonderful! Creativity makes life beautiful."
    elif hobby in ["reading", "writing"]:
        return "📚 Excellent! Knowledge and imagination build strong minds."
    else:
        return "✨ That’s a unique hobby! Keep nurturing your passion."


def generate_message(name, age, hobby):
    category = categorize_age(age)

    if category == "Invalid":
        return "❌ Invalid age entered. Please restart and enter a valid age."

    base_message = f"\n🌟 Hello {name}!\nYou are {age} years old ({category}).\n"

    # Category-based personalized advice
    if category == "Child":
        advice = "Enjoy learning new things and have fun exploring the world! 🌈"
    elif category == "Teenager":
        advice = "This is the time to build skills and dream big! 🚀"
    elif category == "Young Adult":
        advice = "Focus on growth, career goals, and self-development! 💎"
    elif category == "Adult":
        advice = "Balance work, passion, and personal growth wisely. ⚖"
    else:
        advice = "Your experience is your strength. Keep inspiring others! 🌟"

    hobby_msg = hobby_response(hobby)

    final_message = f"""
{base_message}

You enjoy: {hobby}
{hobby_msg}

Advice for you:
{advice}

Keep growing and shining! ✨
"""

    return final_message


def main():
    print("====== Smart Input Program (Advanced) ======")

    name = input("Enter your name: ")

    
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("⚠ Please enter a valid number for age.")

    hobby = input("Enter your hobby: ")

    result = generate_message(name, age, hobby)
    print(result)


if __name__ == "__main__":
    main()