"""PayPilot money guides, part A: UAE, Dubai budgeting, NRIs, India."""

GUIDES_A = [
{
"slug": "best-expense-tracker-app-uae",
"title": "Expense Tracker App for the UAE: AED Spending, Cards and Bills",
"desc": "Track spending in the UAE: AED salary, rent cheques, DEWA and telecom bills, credit cards, foreign charges, and what a good expense app should handle.",
"category": "UAE",
"tags": "UAE Tracking",
"lede": "Money in the UAE moves in a particular rhythm: one salary in dirhams, rent in a few large cheques, a lot of card spending, and the occasional charge in another currency. A tracker that fits that rhythm is worth more than one with the longest feature list.",
"sections": [
("quick-answer", "Quick answer", """
<p>Pick a tracker that can read alerts from UAE banks so card and transfer spending shows up without typing, lets you set AED as the home currency, keeps rent and annual bills visible as commitments, and does not need your bank login. Then give it one full salary cycle before you judge your numbers.</p>
<div class="callout"><p><strong>The test:</strong> after a month, can you say what you spent in AED, what is already committed for next month, and which card each purchase went on?</p></div>
"""),
("uae-pattern", "What makes UAE spending different", """
<p>Generic budgeting advice assumes rent is paid every month and most spending is cash or debit. In the UAE, a few things break that assumption:</p>
<ul>
<li><strong>Rent in cheques.</strong> Many leases are paid in one to four post-dated cheques a year. A AED 72,000 rent paid in four cheques is AED 18,000 leaving your account every three months, not AED 6,000 every month. If your tracker only sees the month the cheque clears, three months look rich and one looks like a disaster.</li>
<li><strong>Cards everywhere.</strong> Groceries, fuel, food delivery and subscriptions usually go on a credit card, so spending and paying are two separate events. The purchase is the expense; paying the card bill later is a transfer.</li>
<li><strong>Utility and telecom bills.</strong> DEWA, ADDC, SEWA or Etihad WE for power and water, plus an Etisalat (e&amp;) or du bill, recur monthly but vary with the season. Summer power bills can be several times a winter one.</li>
<li><strong>Charges in other currencies.</strong> Trips home, online shopping and app stores can bill in INR, USD, GBP or EUR. What matters for your budget is the AED amount that reached your card, including any foreign transaction fee.</li>
<li><strong>VAT is already included.</strong> Shelf prices and receipts include 5% VAT, so you never need to add it when logging an amount.</li>
</ul>
"""),
("checklist", "What to check before you choose an app", """
<table><thead><tr><th>Need</th><th>Why it matters here</th><th>What to look for</th></tr></thead><tbody>
<tr><td>Reads UAE bank alerts</td><td>Most purchases are card taps and online payments</td><td>Works with SMS or app notifications from your actual bank, and lets you test one message</td></tr>
<tr><td>AED home currency</td><td>Totals should be in the currency you are paid in</td><td>A home-currency setting, plus the ability to record other currencies</td></tr>
<tr><td>Recurring commitments</td><td>Rent cheques, school fees and insurance are lumpy</td><td>Scheduled payments with reminders before the due date</td></tr>
<tr><td>Card identification</td><td>Many people carry two or three cards</td><td>Purchases tagged with the card's last four digits</td></tr>
<tr><td>No bank login</td><td>Fewer credentials stored by third parties</td><td>Capture from alerts or manual entry, not stored banking passwords</td></tr>
<tr><td>Honest pricing</td><td>Subscriptions add up, which is what you are trying to control</td><td>Clear free tier; one-time purchase or a price you can see upfront</td></tr>
</tbody></table>
"""),
("foreign", "How to record foreign-currency charges", """
<p>When you pay INR 4,000 for a hotel in Kochi on a UAE card, the bank alert usually shows the AED amount debited, sometimes alongside the original amount. Log the AED figure as the expense, because that is what left your account. Put the original amount and currency in the note if you want to remember it.</p>
<p>Two things trip people up. First, the AED figure in the first alert can differ slightly from the statement, because the final rate is set when the merchant settles. Correct the amount if it changes by more than a few dirhams. Second, cards often add a foreign transaction fee, sometimes shown as a separate line. Treat it as part of the cost of that purchase, not as a mystery bank charge.</p>
"""),
("setup", "A 20-minute setup for your first salary cycle", """
<ol class="steps">
<li>Set AED as the home currency.</li>
<li>Add your rent as a recurring payment on each cheque date, with the full cheque amount.</li>
<li>Add fixed monthly bills: phone, internet, gym, school transport, any car loan.</li>
<li>Turn on automatic capture for your bank alerts (on iPhone this is a one-time Shortcuts setup; on Android it is notification access).</li>
<li>Log cash spending by hand for one month. It is usually smaller than people expect, but taxis, tips and small shops add up.</li>
<li>At month end, compare what you spent with your salary, then put a monthly amount aside for the next rent cheque.</li>
</ol>
<p>If you want to plan the split before you start, the <a href="../budget-calculator">salary budget calculator</a> works in AED and shows a daily safe-to-spend figure.</p>
"""),
("paypilot", "Where PayPilot fits", """
<p>PayPilot reads payment SMS from banks in the UAE and India, on the phone, and logs debits as expenses. On iPhone that runs through Shortcuts automations for bank SMS, Apple Pay taps and bank app notifications; on Android it uses notification access. It never logs into your bank. Rent, bills and subscriptions sit in the Payments tab with reminders, and each card purchase keeps the last four digits so you can see which card it was on.</p>
<p>Expenses, recurring payments, subscriptions, loans, budgets, reminders and automatic capture are free. PayPilot Credit is an optional one-time purchase that adds income tracking, your monthly net, safe-to-spend and cash-flow reports.</p>
"""),
],
"faq": [
("Does PayPilot work with UAE banks?", "Automatic capture is built around the payment SMS banks send, from any bank in the UAE or India. If your bank wording is unusual, use Settings → Auto-capture → Test a bank message to see what would be logged."),
("Is there a free budget app for the UAE that does not need my bank login?", "Yes. PayPilot's core features, including automatic capture of spending and budgets, are free and work from alerts on your phone rather than a bank connection."),
("Should I budget rent monthly or per cheque?", "Both. Record each cheque on the date it clears, and set aside one twelfth of the annual rent every month so the cheque never lands on an empty account."),
("Can I track AED and INR in the same app?", "Yes. Set AED as your home currency and record INR spending in INR when it happens in India. For a fuller two-country method, see the NRI guide."),
],
"related": ["dubai-salary-budget", "nri-expense-tracker-uae-india", "credit-card-spending-tracker"],
},
{
"slug": "dubai-salary-budget",
"title": "How to Budget a Dubai Salary: Rent Cheques, Bills and Annual Costs",
"desc": "A worked Dubai salary budget: turning rent cheques, school fees, insurance and flights home into monthly amounts, plus how to handle card instalment plans.",
"category": "Dubai",
"tags": "UAE Tracking",
"lede": "Most Dubai budgets fail on the big, irregular payments, not the daily ones. Rent cheques, annual insurance, visa renewals and the summer flight home are predictable, but they do not arrive monthly. The fix is to turn each one into a monthly amount you set aside.",
"sections": [
("quick-answer", "Quick answer", """
<p>List every cost that is not monthly, divide each by the number of months until it is due, and treat the result as a fixed monthly bill. What remains after fixed bills and those set-asides is your real spending money. Budget from that, not from your balance on payday.</p>
"""),
("example", "A worked example on AED 15,000 a month", """
<p>The figures below are illustrative, not a recommendation. Swap in your own.</p>
<table><thead><tr><th>Item</th><th>How it is paid</th><th>Monthly amount</th></tr></thead><tbody>
<tr><td>Rent, AED 66,000 a year</td><td>4 cheques of AED 16,500</td><td>AED 5,500 set aside</td></tr>
<tr><td>DEWA (power and water)</td><td>Monthly, higher in summer</td><td>AED 550 average</td></tr>
<tr><td>Phone and home internet</td><td>Monthly</td><td>AED 520</td></tr>
<tr><td>Transport (metro, Salik, parking, fuel)</td><td>Ongoing</td><td>AED 900</td></tr>
<tr><td>Groceries and household</td><td>Ongoing</td><td>AED 1,800</td></tr>
<tr><td>Car insurance and registration</td><td>Once a year, about AED 3,000</td><td>AED 250 set aside</td></tr>
<tr><td>Flights home in summer</td><td>Once a year, about AED 4,800</td><td>AED 400 set aside</td></tr>
<tr><td>Savings and remittance</td><td>On payday</td><td>AED 3,000</td></tr>
<tr><td><strong>Left for everything else</strong></td><td></td><td><strong>AED 2,080</strong></td></tr>
</tbody></table>
<p>AED 2,080 for eating out, shopping, subscriptions and surprises is about AED 69 a day. That number is far more useful than "I have AED 15,000," and it is why a rent cheque never has to feel like an emergency.</p>
"""),
("annual", "The annual costs people forget", """
<ul>
<li>Car insurance and Mulkiya renewal, plus any service due at the same time.</li>
<li>Visa and Emirates ID renewals for you or dependants, and medical tests that go with them.</li>
<li>School fees, usually charged per term, and the uniform and book costs at the start of the year.</li>
<li>The annual fee on a credit card after the first year.</li>
<li>Tenancy renewal costs: Ejari registration, agency fees if you move, and a security deposit.</li>
<li>Gifts and travel around Eid, Diwali, Christmas or Onam, which tend to land in the same few weeks every year.</li>
</ul>
<p>Go through last year's statements once, list everything that happened only once or twice, and add each to your plan. It takes an hour and removes most of the year's surprises.</p>
"""),
("instalments", "Card instalment plans: what to record", """
<p>UAE card issuers often offer to convert a large purchase into monthly instalments, sometimes advertised as 0% but with a one-off processing fee. Record it in two parts:</p>
<ol class="steps">
<li>The purchase itself, on the day you bought it, so your spending history is honest.</li>
<li>The monthly instalment as a recurring commitment until it ends, so each month's budget shows the money already promised.</li>
</ol>
<p>Add the processing fee as its own expense. A 0% plan with a AED 199 fee on a AED 3,000 purchase still costs you about 6.6%. The <a href="../emi-calculator">EMI calculator</a> shows the real cost of an instalment plan that charges interest.</p>
"""),
("tracking", "Keeping the budget honest each week", """
<p>A budget is only as good as the records behind it. Once a week, spend five minutes checking that card purchases were captured, cash spending was logged, and nothing was counted twice. Then compare what you have spent so far with the daily figure from your plan. If you are ahead, cut back for the rest of the week rather than waiting for the month to end.</p>
<p>At the end of your contract, your <a href="../uae-gratuity-calculator">end-of-service gratuity</a> is a real lump sum, but it is not part of your monthly budget. Plan it separately.</p>
"""),
("paypilot", "Doing this in PayPilot", """
<p>Add each rent cheque and annual bill as a scheduled payment in the Payments tab, with a reminder a few days before it is due. Card spending from bank SMS is logged automatically, and the monthly budget compares what you spent against your plan. If you buy PayPilot Credit, safe-to-spend subtracts upcoming bills from your income for you.</p>
"""),
],
"faq": [
("How much of a Dubai salary should go on rent?", "There is no fixed rule, but many people aim to keep rent around a third of take-home pay. Above that, the set-asides for annual costs and savings get hard to fit. Work out your own split with the budget calculator."),
("Should I pay rent in one cheque or several?", "One cheque can get you a lower rent, but it ties up a large amount at once. Several cheques are easier on cash flow. Either way, set aside the monthly equivalent so each cheque is covered."),
("How do I track a rent cheque that has not cleared yet?", "Record it as a scheduled payment on the cheque date. When it clears, the bank alert confirms it, and you mark the payment as done."),
],
"related": ["best-expense-tracker-app-uae", "safe-to-spend-calculator", "credit-card-spending-tracker"],
},
{
"slug": "nri-expense-tracker-uae-india",
"title": "Expense Tracking for NRIs and Expats: One Budget Across Two Countries",
"desc": "How NRIs and expats in the UAE can track AED living costs, money sent home, India EMIs and family support without mixing up transfers and spending.",
"category": "NRIs",
"tags": "UAE India Tracking",
"lede": "If you earn in dirhams and still pay for things in India, your money lives in two places. The trick is not more detail. It is deciding which movements are spending and which are just money moving between your own accounts.",
"sections": [
("quick-answer", "Quick answer", """
<p>Keep three groups: money spent living in the UAE, money spent in India (EMIs, family support, bills), and transfers between your own accounts. Only the first two are expenses. A remittance into your own NRE account is a transfer, while a payment to your parents for household costs is an expense. Track both currencies as they happen, and note the rate on each remittance.</p>
"""),
("three-streams", "The three money streams", """
<table><thead><tr><th>Stream</th><th>Examples</th><th>How to treat it</th></tr></thead><tbody>
<tr><td>UAE living costs</td><td>Rent, groceries, transport, phone, card spending</td><td>Expenses in AED</td></tr>
<tr><td>India commitments</td><td>Home loan EMI, insurance premiums, family support, property tax, school fees for children in India</td><td>Expenses in INR, or in AED if paid directly from the UAE</td></tr>
<tr><td>Moving your own money</td><td>Remittance to your NRE or NRO account, card bill payments, moving savings</td><td>Transfers, not spending</td></tr>
</tbody></table>
<p>Mixing these up is the most common reason expat budgets look wrong. Count a AED 5,000 transfer to your own NRE account as spending and your month looks AED 5,000 worse than it was. Then count the EMI paid from that account as well, and the same money is counted twice.</p>
"""),
("remittances", "Recording remittances and exchange rates", """
<p>For each remittance, note three things: the AED that left your UAE account, the INR that arrived, and any fee. The effective rate is INR received divided by AED sent, fee included. Over a year this tells you whether one exchange house or app consistently gives you a better deal, which is often worth more than switching a subscription.</p>
<p>Do not try to convert every Indian expense back into AED at the day's rate. Record INR spending in INR, and compare totals per currency. When you need one combined number, convert monthly totals at the average rate you actually got on your remittances.</p>
"""),
("sms", "Getting Indian bank alerts while you live abroad", """
<p>Automatic tracking depends on the alert reaching your phone. Many NRIs keep an Indian number for OTPs, on a second SIM or eSIM. If that number is active on your phone, Indian bank SMS can be captured the same way as UAE ones. If the Indian SIM sits in a drawer, those alerts never arrive, and you will need to rely on the bank's app notifications or log Indian payments by hand.</p>
<p>Some Indian banks have also stopped sending SMS for small UPI payments and send email instead, so small India-side spending is the part most likely to go missing.</p>
"""),
("trips", "Trips home", """
<p>A month in India can undo a careful UAE budget: flights, gifts, family events and a lot of small UPI and cash spending. Treat the trip as a project with its own budget. Set aside a monthly amount for it in the UAE (see the <a href="dubai-salary-budget">Dubai salary budget</a> guide), then log trip spending in INR while you are there and compare the total with what you saved.</p>
"""),
("checklist", "Monthly NRI checklist", """
<ol class="steps">
<li>Confirm salary received in AED.</li>
<li>Record each remittance with AED sent, INR received and fee.</li>
<li>Check India EMIs and premiums were paid, and that the account they come from has enough balance.</li>
<li>Review UAE spending against your budget.</li>
<li>Note any money lent to family or friends, and repayments received.</li>
</ol>
<p>Questions about NRE versus NRO accounts, or tax in either country, depend on your situation; ask a qualified adviser. This guide is only about keeping clear records.</p>
"""),
("paypilot", "Doing this in PayPilot", """
<p>Set AED as your home currency and record INR amounts in INR. PayPilot reads payment SMS from both UAE and Indian banks, and India EMIs can be added as recurring payments with reminders. Money lent to relatives goes in the Credit tab with each repayment as it comes in.</p>
"""),
],
"faq": [
("Is money sent to my own NRE account an expense?", "No. It is a transfer between your own accounts. It becomes spending only when it is used to pay for something."),
("Is money sent to my parents an expense?", "If it is support for their household costs, yes, record it as family support. If it is a loan you expect back, record it as money lent instead."),
("Which currency should my home currency be?", "The one you are paid in, usually AED. That keeps your monthly budget in the currency your salary arrives in."),
],
"related": ["best-expense-tracker-app-uae", "best-expense-tracker-app-india", "loan-tracker-money-lent"],
},
{
"slug": "best-expense-tracker-app-india",
"title": "Expense Tracker App for India: UPI, Cards and Cash in One Place",
"desc": "How to track UPI, card and cash spending in India without typing every ₹20 payment: bank SMS, UPI app notifications, UPI Lite, ATM cash and EMIs.",
"category": "India",
"tags": "India Tracking",
"lede": "In India the hard part is not big purchases. It is the twenty small UPI payments a day, split across two or three apps, plus cash that leaves no trail. A good tracker catches the digital ones automatically and makes the rest quick to add.",
"sections": [
("quick-answer", "Quick answer", """
<p>Use a tracker that reads your bank's debit SMS and, where SMS does not arrive, your bank or UPI app notifications. Log cash spending by hand, or treat ATM withdrawals as cash spending if you do not want the detail. Add EMIs and subscriptions as recurring payments. Then review once a week, not once a quarter.</p>
"""),
("upi", "Why UPI spending goes missing", """
<p>UPI payments normally trigger a debit SMS from your bank, which is what makes automatic tracking possible. A few situations break that:</p>
<ul>
<li><strong>Small-payment SMS cut-offs.</strong> Some banks have stopped sending SMS for low-value UPI payments and send email instead. HDFC Bank, for example, stopped SMS alerts for UPI payments of ₹100 or less in 2024.</li>
<li><strong>UPI Lite.</strong> Payments from the UPI Lite on-device wallet do not send an SMS each time. Your bank sends one summary SMS a day, and your statement only shows the top-up.</li>
<li><strong>Wallet balances.</strong> Spending from a wallet balance (Paytm, Amazon Pay and similar) is not a bank debit, so your bank sends nothing.</li>
<li><strong>Multiple apps.</strong> GPay, PhonePe, Paytm and your bank's own app can all pay from the same account. The bank SMS is the one thing they have in common.</li>
</ul>
<p>The practical answer: let bank SMS do most of the work, add notification capture from your UPI apps if your bank skips small payments, and treat a UPI Lite or wallet top-up as one cash-like amount you spend down.</p>
"""),
("cash", "Handling cash without logging every rupee", """
<p>You have two honest options. Log each cash spend as it happens, which gives the most detail. Or record the ATM withdrawal itself as a "cash" expense and stop there. The second is less precise, but your monthly total stays correct, and for most people the detail of where ₹2,000 of cash went is not worth the effort. Do not do both, or the same money is counted twice.</p>
"""),
("budget", "A simple first budget in INR", """
<table><thead><tr><th>Bucket</th><th>What goes in it</th></tr></thead><tbody>
<tr><td>Fixed</td><td>Rent, EMIs, insurance premiums, phone and broadband, school fees</td></tr>
<tr><td>Everyday</td><td>Groceries, fuel, food delivery, auto and cab rides, small UPI payments</td></tr>
<tr><td>Occasional</td><td>Clothes, gadgets, travel, festivals and weddings</td></tr>
<tr><td>Future you</td><td>SIPs, RD, emergency fund</td></tr>
</tbody></table>
<p>Start by recording one month without changing anything. Then set a monthly limit for Everyday and Occasional based on what actually happened, not what you wish had happened. Pay Future you on salary day, before the Everyday money starts going.</p>
"""),
("emi", "EMIs and recurring debits", """
<p>Loan EMIs, SIPs, insurance and OTT subscriptions are often auto-debited through an e-mandate. Under RBI rules your bank or card issuer must send a pre-debit notification before each recurring charge, which gives you a chance to stop one you no longer want. Add each one to your tracker as a recurring payment so the month's commitments are visible on day one. The <a href="../emi-calculator">EMI calculator</a> shows how much of each EMI is interest.</p>
"""),
("compare", "What to compare when choosing an app", """
<ul>
<li><strong>Capture:</strong> does it read SMS from your bank, and can it read UPI app notifications too?</li>
<li><strong>Privacy:</strong> is the message read on your phone, or uploaded to a server? Does it ignore OTPs?</li>
<li><strong>Corrections:</strong> can you fix a category or amount in one tap?</li>
<li><strong>Duplicates:</strong> if both the SMS and the app notification arrive, does it log the payment once?</li>
<li><strong>Cost:</strong> is automatic capture free, or locked behind a subscription?</li>
</ul>
"""),
("paypilot", "Where PayPilot fits", """
<p>PayPilot reads debit SMS from Indian banks on your phone and logs them as expenses, including the merchant and the card's last four digits where the message has them. It can also read payment notifications from bank and UPI apps (on Android through notification access, on iPhone through a Shortcuts automation), and it skips the duplicate when two alerts describe the same payment. OTPs and promotional messages are ignored. Expenses, budgets, EMIs as recurring payments, and automatic capture are free.</p>
"""),
],
"faq": [
("Why are my small UPI payments not being tracked?", "Your bank may not send SMS for small UPI payments, or you may be paying from UPI Lite, which sends one daily summary instead. Add notification capture from your UPI app, or log those payments by hand."),
("Is there a free expense tracker for India that reads SMS automatically?", "Yes. PayPilot's automatic capture of bank SMS is part of the free app."),
("Should ATM withdrawals count as spending?", "Only if you are not also logging each cash purchase. Pick one method and stick with it so the money is not counted twice."),
("Does the app need my net banking password?", "No. PayPilot works from the alerts your bank already sends to your phone."),
],
"related": ["automatic-expense-tracker-bank-sms", "subscription-tracker-monthly-bills", "nri-expense-tracker-uae-india"],
},
]
