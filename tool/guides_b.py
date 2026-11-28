"""PayPilot money guides, part B: automatic capture, privacy, subscriptions, loans."""

GUIDES_B = [
{
"slug": "automatic-expense-tracker-bank-sms",
"title": "How Automatic Expense Tracking Works: Bank SMS, Notifications and Apple Pay",
"desc": "How expense apps turn bank SMS, bank and UPI app notifications and Apple Pay taps into records on iPhone and Android, what gets missed, and how to test it.",
"category": "Automatic tracking",
"tags": "Tracking",
"lede": "Automatic tracking is not magic and it is not a bank connection. It works by reading the payment alerts that already arrive on your phone. Knowing which alerts arrive, and which do not, tells you exactly what will be captured.",
"sections": [
("quick-answer", "Quick answer", """
<p>There are three sources: bank SMS, notifications from bank and UPI apps, and Apple Pay taps in shops. On iPhone each one is a Shortcuts automation you set up once. On Android, the app reads payment notifications after you grant notification access. Together they catch most card, UPI and transfer spending. Cash, some small UPI payments and wallet balances still need a quick manual entry.</p>
"""),
("sources", "The three capture sources compared", """
<table><thead><tr><th>Source</th><th>Catches</th><th>Misses</th><th>Set up on</th></tr></thead><tbody>
<tr><td>Bank SMS</td><td>Card, UPI and transfer debits and credits from almost any bank</td><td>Payments your bank does not text about</td><td>iPhone: Shortcuts "When I receive a message". Android: notification access</td></tr>
<tr><td>Bank and UPI app notifications</td><td>Banks that notify in their app instead of SMS, and small UPI payments some banks no longer text about</td><td>Apps with notifications turned off</td><td>iPhone: Shortcuts "When I receive a notification". Android: notification access</td></tr>
<tr><td>Apple Pay (Wallet)</td><td>Card taps at a shop, with amount and merchant</td><td>Apple Pay inside apps and on websites; iOS only triggers the automation for in-store taps</td><td>iPhone only: Shortcuts "When any card is tapped"</td></tr>
</tbody></table>
<p>Online Apple Pay payments are not lost. Your bank still sends an SMS or app notification for them, so the first two sources pick them up.</p>
"""),
("iphone", "On iPhone: why it uses Shortcuts", """
<p>iOS does not let apps read your messages. The only route is a Shortcuts personal automation that you create, which passes a matching message to the app. That limits what an app can see: only the texts that match your filter are handed over.</p>
<p>PayPilot's bank SMS automation uses the filter "Message contains ited", which matches debited, credited and deposited, so a single automation catches money going out and coming in. Messages with words like "limited" or "invited" also match. They are read on the phone, recognised as non-payments, and dropped without being saved. If your bank uses other wording, such as "spent" or "UPI debit:", add a second copy of the automation with that word. The <a href="../auto-capture">auto-capture guide</a> has screenshots for every step, and the <a href="../sms-expense-tracker-iphone">iPhone SMS tracker page</a> explains the setup in brief.</p>
"""),
("android", "On Android: notification access", """
<p>Android lets an app read notifications once you allow it in settings. With notification access on, PayPilot reads payment notifications from your SMS app, bank apps and UPI apps on the phone. It does not read chats or email. There is nothing to build: open Settings → Auto-capture in the app and tap Allow notification access.</p>
"""),
("parsing", "What happens to a message once it is read", """
<ol class="steps">
<li>The message is checked on the phone: is it a payment, and is it money in or out?</li>
<li>OTPs, offers and messages without an account or payment reference are discarded.</li>
<li>For a payment, the amount, merchant, date and last four card digits are extracted.</li>
<li>If the same payment already arrived from another source (say SMS and Apple Pay), the repeat is skipped.</li>
<li>The record is saved, and the message text itself is deleted. Nothing is sent to a server or an AI to read it.</li>
</ol>
<p>Two genuinely different payments that look identical, like two coffees of the same price a minute apart, are both kept. If one is a mistake, delete it.</p>
"""),
("test", "How to test it before you rely on it", """
<p>In PayPilot, open Settings → Auto-capture → Test a bank message and paste a real SMS from your bank. It shows exactly what would be logged, or why not. After your next real payment you should get a notification such as "Auto-captured ₹250.00 · Swiggy". Tap it to check the category.</p>
<p>If nothing appears after a payment, check that the automation is on and Confirm Before Run is off, that the message contains your filter word, and then open the app once: items captured while it was closed are added when it opens.</p>
"""),
("gaps", "What still needs a manual entry", """
<ul>
<li>Cash.</li>
<li>UPI Lite payments, which get one daily summary SMS instead of one per payment.</li>
<li>Spending from wallet balances such as Paytm or Amazon Pay.</li>
<li>Bank alerts that arrive on a SIM that is not in your phone.</li>
</ul>
<p>For most people that is a handful of entries a week, against dozens captured automatically.</p>
"""),
],
"faq": [
("Does automatic expense tracking need my bank login?", "No. It reads the alerts your bank already sends to your phone. No bank credentials are involved."),
("Why was an online Apple Pay payment not captured by the Wallet automation?", "iOS only runs Wallet automations for in-store taps. Online and in-app Apple Pay payments are captured from your bank's SMS or app notification instead."),
("Will a payment be logged twice if I get both an SMS and an app notification?", "No. PayPilot recognises the repeat and keeps one record."),
("Does it work with Indian and UAE banks?", "Yes. The bank SMS parser handles messages from banks in both countries. Use the in-app test to check your bank's wording."),
],
"related": ["is-sms-expense-tracker-safe", "best-expense-tracker-app-india", "best-expense-tracker-app-uae"],
},
{
"slug": "is-sms-expense-tracker-safe",
"title": "Is an SMS Expense Tracker Safe? Privacy, Permissions and Bank Sync Compared",
"desc": "How SMS expense trackers compare with bank sync and manual entry on privacy, access and risk, plus questions to ask before granting permissions.",
"category": "Privacy and safety",
"tags": "Privacy Comparisons Tracking",
"lede": "Any finance app that tracks spending automatically has to see something about your money. The real question is what it sees, where that data goes, and how easily you can switch it off. Those answers differ a lot between apps.",
"sections": [
("quick-answer", "Quick answer", """
<p>An SMS tracker can be a low-access option if three things are true: it reads messages on your phone rather than uploading them, it throws away OTPs and anything that is not a payment, and it never asks for your bank login. Check those three before you grant any permission.</p>
"""),
("models", "Three ways apps get your transactions", """
<table><thead><tr><th></th><th>Manual entry</th><th>Alerts (SMS and notifications)</th><th>Bank connection</th></tr></thead><tbody>
<tr><td>What the app can access</td><td>Only what you type</td><td>The payment alerts you allow</td><td>Account data shared through the connection</td></tr>
<tr><td>Bank credentials involved</td><td>None</td><td>None</td><td>Consent through a provider, or in some apps your login</td></tr>
<tr><td>Coverage</td><td>Whatever you remember</td><td>Every payment your bank alerts you about</td><td>Every transaction on connected accounts</td></tr>
<tr><td>Typical failure</td><td>You stop logging</td><td>A bank changes its wording or stops an alert</td><td>The connection expires or breaks</td></tr>
<tr><td>How to switch off</td><td>Stop using it</td><td>Delete the automation or revoke notification access</td><td>Revoke consent with the provider and the app</td></tr>
</tbody></table>
<p>In India, bank connections increasingly run through the RBI's Account Aggregator framework, where you approve each data share and can revoke it. That is safer than handing an app your net banking password, which you should never do. But even a consent-based connection shares your full transaction history, which is more than alert-based tracking needs.</p>
"""),
("questions", "Questions to ask before granting permission", """
<ol class="steps">
<li><strong>Where is the message read?</strong> On the phone is better than uploaded to a server for parsing.</li>
<li><strong>What is kept?</strong> Ideally just the amount, merchant, date and the last four card digits, not the full message.</li>
<li><strong>What happens to OTPs?</strong> They should be recognised and discarded immediately, never stored.</li>
<li><strong>Which messages can it see?</strong> On iPhone, only those your automation passes. On Android, check whether it reads only payment notifications or everything.</li>
<li><strong>Is cloud backup encrypted, and by whom?</strong> Encryption on the device before upload is the stronger design.</li>
<li><strong>Can you delete everything?</strong> There should be an in-app account deletion and a web route if you lose the phone.</li>
<li><strong>Does it send data to an AI service?</strong> If so, what, and can you opt out?</li>
</ol>
"""),
("paypilot", "How PayPilot answers those questions", """
<ul>
<li>PayPilot cannot open your messages. On iPhone, iOS only hands over the texts and notifications your automations select.</li>
<li>Messages are read on the phone. The text is never uploaded or sent to a server or AI, and it is deleted as soon as it is read.</li>
<li>OTPs are recognised and thrown away immediately.</li>
<li>Only the expense is kept: amount, merchant, date and the last four card digits.</li>
<li>Records are stored on your device. If you sign in and turn on sync, they are encrypted on the device before being written to the cloud.</li>
<li>It does not connect to your bank, and never asks for bank credentials.</li>
<li>You can delete your account in Settings, or through the <a href="../delete-account">account deletion page</a>.</li>
</ul>
<p>No design can promise absolute security. Keep your phone locked, protect the account you sign in with, and read the <a href="../privacy">privacy policy</a> for the full details.</p>
"""),
("never", "What you should never share with any finance app", """
<ul>
<li>Net banking passwords or card PINs.</li>
<li>OTPs, even if an app or a caller says it needs one to "verify" something.</li>
<li>Full card numbers and CVV codes, except in a genuine payment form.</li>
</ul>
<p>A tracking app has no reason to ask for any of these. If one does, do not use it.</p>
"""),
],
"faq": [
("Can an SMS expense tracker read my OTPs?", "On iPhone, only messages your automation passes reach the app; PayPilot discards OTPs immediately and never stores them. On Android, check which notifications the app reads and what it does with them."),
("Is bank sync safer than SMS tracking?", "Not necessarily. Consent-based bank connections avoid sharing your password, but they share your full transaction history. Alert-based tracking shares less and needs no bank credentials at all."),
("How do I stop an SMS tracker reading my messages?", "On iPhone, delete the automation in Shortcuts. On Android, turn off the app's notification access in system settings."),
],
"related": ["automatic-expense-tracker-bank-sms", "money-manager-alternative-automatic", "best-expense-tracker-app-india"],
},
{
"slug": "subscription-tracker-monthly-bills",
"title": "Subscription Tracker: Find, Audit and Cut Recurring Charges",
"desc": "Find every subscription and recurring bill, see its yearly cost, decide what to keep, and cancel on iPhone, Android or your card: a 30-minute audit.",
"category": "Subscriptions",
"tags": "Tracking",
"lede": "Subscriptions are designed to be easy to start and easy to forget. Individually they look small. Together, and counted over a year, they are often one of the larger lines in a budget. A short audit, then a simple tracker, keeps them under control.",
"sections": [
("quick-answer", "Quick answer", """
<p>List every recurring charge from the last three months of card and bank statements, plus your App Store or Google Play subscriptions. Multiply each by 12 to see its yearly cost. Cancel anything you would not sign up for again today, and put the rest in a tracker with a reminder before each renewal.</p>
"""),
("hiding", "Where subscriptions hide", """
<ul>
<li><strong>App store billing.</strong> Subscriptions bought inside apps are billed by Apple or Google, so your statement says "Apple" or "Google", not the app's name.</li>
<li><strong>Annual renewals.</strong> A yearly charge shows up once, so it never feels like a habit. It is the one most likely to surprise you.</li>
<li><strong>Free trials.</strong> Most turn into paid plans automatically unless you cancel before the trial ends.</li>
<li><strong>Bundles.</strong> Telecom plans and card benefits sometimes include a streaming service that you may also be paying for separately.</li>
<li><strong>Family members.</strong> A service someone else in the house also pays for.</li>
</ul>
"""),
("audit", "The 30-minute audit", """
<ol class="steps">
<li>Open three months of card and bank statements and mark every charge that repeats.</li>
<li>On iPhone, open Settings, tap your name, then Subscriptions. On Android, open Google Play, tap your profile, then Payments &amp; subscriptions.</li>
<li>Write each one down with its price and how often it bills.</li>
<li>Convert each to a yearly cost.</li>
<li>For each, ask: did I use it in the last month, and would I sign up today at this price?</li>
<li>Cancel or downgrade the ones that fail. Put the rest in your tracker.</li>
</ol>
"""),
("yearly", "Why the yearly number changes decisions", """
<table><thead><tr><th>Subscription</th><th>Monthly</th><th>Yearly</th></tr></thead><tbody>
<tr><td>Second streaming service</td><td>AED 35</td><td>AED 420</td></tr>
<tr><td>Cloud storage upgrade</td><td>AED 11</td><td>AED 132</td></tr>
<tr><td>Fitness app</td><td>₹399</td><td>₹4,788</td></tr>
<tr><td>Music premium</td><td>₹119</td><td>₹1,428</td></tr>
</tbody></table>
<p>"AED 35" sounds like nothing. "AED 420 a year for a service I opened twice" sounds like a decision. Seeing the yearly cost is usually enough to make the call.</p>
"""),
("rules", "Keep, pause or cancel", """
<ul>
<li><strong>Keep</strong> what you use every week and would miss.</li>
<li><strong>Rotate</strong> streaming services: keep one at a time and switch when you have finished what you wanted to watch.</li>
<li><strong>Switch to yearly billing</strong> only for services you are certain to keep, and set a reminder before the renewal.</li>
<li><strong>Cancel</strong> anything you are keeping "just in case". You can usually sign up again in a minute.</li>
</ul>
"""),
("india-uae", "Recurring card charges in India and the UAE", """
<p>In India, recurring card and UPI charges run on e-mandates, and RBI rules require a pre-debit notification before each charge. That notification is your last chance to cancel. Mandates can also be viewed and cancelled from your bank or UPI app. In the UAE, recurring charges are usually stored card payments; cancel with the merchant first, and if the charges continue, ask your bank about blocking them.</p>
"""),
("paypilot", "Tracking subscriptions in PayPilot", """
<p>Add each subscription in the Payments tab with its price and billing cycle, and PayPilot reminds you before it renews. The monthly view shows how much of your spending is already committed to subscriptions before the month starts. Subscription tracking is free.</p>
"""),
],
"faq": [
("How do I see all my subscriptions on iPhone?", "Open Settings, tap your name, then Subscriptions. That lists everything billed through Apple. Subscriptions paid directly by card are on your card statement instead."),
("How do I cancel a subscription on Android?", "Open Google Play, tap your profile picture, choose Payments & subscriptions, then Subscriptions, and cancel the one you no longer want."),
("Is monthly or yearly billing better?", "Yearly is cheaper only if you would have kept the service all year. If you are not sure, stay monthly."),
],
"related": ["safe-to-spend-calculator", "credit-card-spending-tracker", "best-expense-tracker-app-india"],
},
{
"slug": "loan-tracker-money-lent",
"title": "How to Track Money Lent to Friends and Family (and Every Repayment)",
"desc": "Keep informal loans clear: what to record, logging partial repayments and overpayments, forgiving the rest, and reminding someone without awkwardness.",
"category": "Loans",
"tags": "Tracking",
"lede": "Lending to friends and family rarely goes wrong because someone is dishonest. It goes wrong because nobody wrote anything down, three partial repayments later both people remember a different number, and a simple question becomes awkward.",
"sections": [
("quick-answer", "Quick answer", """
<p>Write down who, how much, when, and when it is due back, at the moment you lend. Record every repayment as its own entry, never by editing the original amount. Then the outstanding balance is always the original amount minus the repayments, and you can show the history if anyone asks.</p>
"""),
("record", "What to record when you lend", """
<table><thead><tr><th>Field</th><th>Why</th></tr></thead><tbody>
<tr><td>Person</td><td>Obvious, but use the name you will search for later</td></tr>
<tr><td>Amount and currency</td><td>Lending AED and being repaid in INR is common; note both</td></tr>
<tr><td>Date lent</td><td>Starts the timeline</td></tr>
<tr><td>Expected repayment</td><td>A date, or "₹5,000 a month from March"</td></tr>
<tr><td>How it was paid</td><td>Bank transfer, UPI or cash. A transfer reference settles disputes</td></tr>
<tr><td>Note</td><td>What it was for. Months later this matters more than you think</td></tr>
</tbody></table>
"""),
("example", "A worked example with partial repayments", """
<table><thead><tr><th>Date</th><th>Entry</th><th>Outstanding</th></tr></thead><tbody>
<tr><td>5 Jan</td><td>Lent ₹40,000 to Arun for a deposit</td><td>₹40,000</td></tr>
<tr><td>2 Feb</td><td>Repaid ₹10,000</td><td>₹30,000</td></tr>
<tr><td>6 Mar</td><td>Repaid ₹10,000</td><td>₹20,000</td></tr>
<tr><td>1 May</td><td>Repaid ₹15,000</td><td>₹5,000</td></tr>
<tr><td>3 Jun</td><td>Repaid ₹5,000</td><td>Settled</td></tr>
</tbody></table>
<p>If you had simply changed "₹40,000" to "₹20,000" in March, you would lose the history. Separate entries mean you can show Arun exactly what has been received, and he can check it against his own transfers.</p>
"""),
("edge", "Overpayments, forgiveness and money you borrowed", """
<ul>
<li><strong>Overpaid?</strong> Record the repayment as received, then either return the extra or note it as credit towards something else. Do not let the balance go negative silently.</li>
<li><strong>Forgiving the rest?</strong> Record a final entry such as "₹3,000 forgiven" so the loan closes cleanly and you are not reminded about it forever.</li>
<li><strong>You borrowed?</strong> Track it the same way in the other direction. Knowing exactly what you owe is part of being easy to lend to.</li>
</ul>
"""),
("reminders", "Reminding someone without making it awkward", """
<p>Agree on the repayment plan when you lend, ideally in a message, so a later reminder refers back to something you both said. When a payment is late, a short, factual note works best: "Hi, just checking on the ₹10,000 for March. I have ₹20,000 outstanding after the last one." The number is the reminder; you do not need to add pressure.</p>
<p>A formal loan with interest, or a large sum, is different. Put it in writing and consider professional advice. The <a href="../emi-calculator">EMI calculator</a> can show what a fair monthly repayment looks like.</p>
"""),
("paypilot", "Tracking loans in PayPilot", """
<p>The Credit tab keeps money lent and money owed in one place. Each loan has its own timeline, partial repayments are added as separate entries, and the outstanding balance updates without you editing the original amount. You can set a reminder for the next expected repayment. Loan tracking is part of the free app.</p>
"""),
],
"faq": [
("Should I charge interest when lending to family?", "That is a personal choice. If you do, agree the rate and repayment plan in writing at the start."),
("What if they repay in a different currency?", "Record the repayment in the currency you received, and note the amount it covers in the loan's currency so the balance stays correct."),
("How do I close a loan I have decided to forgive?", "Add a final entry for the forgiven amount. The loan closes with a full history showing what was repaid and what was written off."),
],
"related": ["credit-card-spending-tracker", "nri-expense-tracker-uae-india", "safe-to-spend-calculator"],
},
]
