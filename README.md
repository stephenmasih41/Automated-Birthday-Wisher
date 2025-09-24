# 🎂 Automated Birthday Wisher (Day 32 – Python Bootcamp)

Welcome to my **Day 32** project of the Python Bootcamp! 🎉  
This project is an **Automated Birthday Wisher** 📨 that checks a CSV file of birthdays every day and sends an email with a random birthday greeting to the lucky person.

---

## ✨ How It Works

1. **📂 Imports**

   - `pandas` → to read the CSV file of birthdays
   - `datetime` → to get today’s date
   - `random` → to pick a random template
   - `smtplib` → to send emails through Gmail

2. **📑 Data Source**

   - A `birthdays.csv` file stores the birthdays with columns like `name`, `email`, `day`, and `month`.

3. **📆 Date Check**

   - The script gets today’s **month** and **day** using `datetime.now()`.
   - It compares today’s date with the CSV to find all people who have birthdays today.

4. **👥 Multiple Birthdays**

   - If multiple people have birthdays on the same day, it stores them in a list (`birthday_people`).
   - Then it loops through each person to send their email.

5. **📜 Random Letter Template**

   - Three letter templates live inside the `letter_templates` folder.
   - The script randomly chooses one, replaces `[NAME]` with the real person’s name, and personalizes the greeting.

6. **📧 Sending Emails**
   - Using `smtplib`, the program logs into Gmail with your email + app password 🔑.
   - Sends a "Happy Birthday" email 🎂 to the right person.

---

## ⚠️ Important Notes

- **🔒 Security**: The email and password are hardcoded here for simplicity. In real projects, always use **environment variables** instead of storing passwords in code.
- **🌍 Automation**: Although the script is automated, it doesn’t run 24/7 for 365 days because:
  - It’s not deployed on the **cloud**.
  - It doesn’t run in the **background scheduler**.

---

## 🏁 Conclusion

This was my **Day 32 project** of the Python Bootcamp! 💻  
It was a great way to practice working with:

- CSVs (`pandas`)
- Date handling (`datetime`)
- File handling
- Automating tasks
- Sending emails with Python
