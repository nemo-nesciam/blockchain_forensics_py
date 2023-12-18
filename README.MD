
# [Detecting Malicious Accounts in Permissionless Blockchains Using Temporal Graph Properties](https://appliednetsci.springeropen.com/articles/10.1007/s41109-020-00338-3)

### Bursts: 
These indicate sudden spikes in activity, which can be in transaction count, balance, or transaction fees. A high number of transactions in a short period, large transactions, or abnormally high transaction fees are signs of potential malicious activity.
- Number of Degree Burst Instances: This refers to the number of times an account experiences a sudden and significant increase in its degree, which is the number of transactions (either incoming or outgoing).

- Largest Burst At: This metric records the time at which the largest burst in degree occurred for an account. This helps in identifying the most significant periods of unusual activity for further investigation.

- Balance Burst: This occurs when transactions involve sums of cryptocurrency that are very large, exceeding a predefined threshold value (θbi). Such large transactions are often linked to illegal activities, such as those found in accounts associated with the Silk Road or involved in money laundering.

- Number of Unique Balance Burst Instances: This is the count of distinct occasions on which the account's transaction balance exceeds the threshold θbi.

- Number of Transactions More Than θbi: This refers to the total number of transactions an account has conducted that are above the threshold value.
  - Temporal Burst Threshold (θti): This threshold is used to determine if a transaction is part of a burst based on the time interval between transactions. If the time between transactions is less than θti, it is considered a burst. However, the exact value of θti is not specified in the quoted text.

  - Degree Burst Threshold (θdi): This threshold is set to 80% of the maximum degree (inDegree or outDegree) observed for an account. In simple terms, if the number of transactions (either incoming or outgoing) at a certain time is more than 80% of the highest number of transactions ever recorded for that account, it's considered unusually high and marked as a burst.

  - Balance Burst Threshold (θbi): Similar to the degree burst, this threshold is 80% of the maximum balance involved in transactions for an account. If the amount of cryptocurrency in a transaction is more than 80% of the highest transaction amount ever recorded for that account, it's flagged as a burst.

  - Gas Price Burst Threshold (θgi): This is 80% of the highest gas price (transaction fee) associated with an account. If the gas price for a transaction is more than 80% of the account's highest ever recorded gas price, it is considered unusual and marked as a burst.  

### Attractiveness: 
This measures an account's engagement with new accounts. High attractiveness suggests an account frequently initiates transactions with different accounts, which could indicate a malicious network. The attractiveness measure is defined as follows:

- Numerator: The number of unique accounts that the target account (account i) has received cryptocurrency from, which were present in the past θa - 1 blocks/times.

- Denominator: The total number of unique accounts from which the account has received cryptocurrency in the last θa blocks.

The attractiveness value is obtained by subtracting this ratio from 1. It's important to note that the in-degree (number of incoming transactions) is specifically considered for this calculation, as most malicious activities involve extracting cryptocurrency from benign accounts.

As blockchain interactions are intermittent and an account's neighborhood is highly dynamic, changing at each epoch (or time block), the attractiveness value also changes over time. This dynamic nature of attractiveness, which reflects the changing patterns of interactions with new accounts, is a key feature in identifying potentially malicious behavior

### Active State: 
Refers to the duration and pattern of account activity. Accounts with irregular or inconsistent activity periods may be suspicious. The historical analysis of attacks on blockchain networks revealed several key characteristics and behaviors of malicious accounts:

1. DDoS Attacks: In a study by Chen et al. (2018a), accounts involved in Distributed Denial of Service (DDoS) attacks were identified. These accounts typically created multiple contracts that were rarely used, indicating malicious intent.

2. Smart Contract (SC) Analysis: Jung et al. (2019) focused on verified SC codes and introduced features such as SC size, lifetime, and average time between transactions (Inter-event time) to identify malicious accounts.

3. Honeypot Deployment and RPC Analysis: Cheng et al. (2019) used honeypots to capture malicious activity and analyzed Remote Procedure Call (RPC) requests to detect suspicious accounts. This method particularly targeted accounts that accepted cryptocurrency from known malicious sources.

4. Behavior Analysis for Crypto-Currency Stealing: This involved identifying accounts engaged in phishing (fisher accounts) and those involved in stealing cryptocurrency.

### Graph-Based Properties: 
Properties like the number of incoming (inDegree) and outgoing (outDegree) transactions help identify unusual transaction patterns often associated with malicious activities. When analyzing the graph-based properties such as the number of incoming (inDegree) and outgoing (outDegree) transactions of accounts on permissionless blockchains, the study focuses on the following aspects:

1. Degree Distribution: The study observes the distribution of inDegree and outDegree across individual accounts. A key observation is the fat-tailed nature of these distributions, indicating that some accounts interact with a larger number of accounts at specific times, leading to bursty behavior.

2. High vs. Low Degree Instances: It was found that the inDegree of very few accounts is exceptionally high (greater than 100) for a few time instances, while most of the time it remains low. This suggests the existence of bursts in account activity. A similar pattern is observed for outDegree.

3. Temporal Bursts: The study also validates the existence of temporal bursts by examining the distribution of inter-event times for all accounts. This analysis reveals that the inter-event time distribution follows a power law, with different parameters for benign and malicious accounts (xmin = 3, α = 1.25 for benign and α = 1.76 for malicious).

When it comes to analyzing balance and transaction fees for identifying malicious accounts in permissionless blockchains, the study focuses on several key features:

Balance Time Series for In/Out Transactions: The study tracks the balance of accounts over time, for both incoming and outgoing transactions. This helps in identifying patterns of fund flow that might indicate suspicious activities.

Maximum Balance (maxInBalance and maxOutBalance): The highest balance for both incoming and outgoing transactions is noted. Large balances, especially in the context of other transactional behaviors, can be indicative of malicious activities.

Zero Balance Transactions: These are transactions where no money was transferred either to or from an account. A high frequency of such transactions can be a red flag for fraudulent activities.

Total Balance: This is the final balance held by the account. Sudden increases or decreases in total balance can signal suspicious activity.

Average Per InBalance (average of received balance): This feature looks at the average balance received by the account, which can highlight unusual patterns in funds received.

Transaction Fees (TF): In cryptocurrency-based blockchains, transactions are marked by fees that a sender is willing to spend. On the Ethereum blockchain, for example, the transaction fee is calculated as Gas × GasPrice. High or unusual transaction fees can be indicative of malicious intentions, such as bribing miners to prioritize transactions or participating in attacks that disrupt the network.

### Balance and Transaction Fees: 
Observing the balance and fees can reveal unusual financial behavior, such as large balances with minimal transactions or high transaction fees, indicating potential malicious intent. When it comes to analyzing balance and transaction fees for identifying malicious accounts in permissionless blockchains, the study focuses on several key features:

1. Balance Time Series for In/Out Transactions: The study tracks the balance of accounts over time, for both incoming and outgoing transactions. This helps in identifying patterns of fund flow that might indicate suspicious activities.

2. Maximum Balance (maxInBalance and maxOutBalance): The highest balance for both incoming and outgoing transactions is noted. Large balances, especially in the context of other transactional behaviors, can be indicative of malicious activities.

3. Zero Balance Transactions: These are transactions where no money was transferred either to or from an account. A high frequency of such transactions can be a red flag for fraudulent activities.

4. Total Balance: This is the final balance held by the account. Sudden increases or decreases in total balance can signal suspicious activity.

5. Average Per InBalance (average of received balance): This feature looks at the average balance received by the account, which can highlight unusual patterns in funds received.

6. Transaction Fees (TF): High or unusual transaction fees can be indicative of malicious intentions, such as bribing miners to prioritize transactions or participating in attacks that disrupt the network.

---

# [Understanding Money Trails of Suspicious Activities in a cryptocurrency-based Blockchain](https://arxiv.org/pdf/2108.11818.pdf)

The study "Understanding Money Trails of Suspicious Activity" identified distinct patterns in the temporal cycles of Gambling, Phishing, and Money Laundering activities on the Ethereum blockchain. Here are the key differences and similarities:

### Gambling:

- In Gambling, the study found that the number of temporal cycles does not significantly increase for money losses greater than 10%. However, for losses less than 10%, there is a significantly higher number of cycles.
- This suggests that in Gambling, the money often moves in patterns where small amounts are lost or won, leading to frequent but relatively minor financial changes​​.

### Phishing:

- Phishing accounts often have very few transactions, which limits their presence in temporal cycles.
- The study noted that the maximum hop-length in cycles involving Phishing accounts was 20, and the money loss along these cyclic paths was often negative, indicating that Phishing accounts tend to receive funds more than they lose.
- This indicates that Phishing activities involve receiving funds more than transferring them, with fewer overall cycles due to the lower number of transactions per account​​.

### Money Laundering:

- Money laundering activities were found to produce more cycles than those involved in Gambling or Phishing.
- The study observed that money laundering-based accounts were more actively involved in cyclic temporal path-based money transfers, with a maximum hop length of 6 in these cycles.
- It was noted that the money loss in these cycles varied, with some showing significantly less loss. The completion time for some cyclic transfers was as short as approximately 3 minutes, indicating rapid movement of funds, which is a characteristic of illicit activities.
- This suggests that Money Laundering involves a more active use of the blockchain for transferring money quickly and in a complex manner, often with varied amounts of money loss.

In summary, while all three activities involve cyclical patterns of money transfer, Gambling is characterized by frequent cycles with smaller financial changes, Phishing by receiving funds in fewer transactions, and Money Laundering by more complex and rapid transfer cycles with variable money loss.

---

[Identification of token contracts on Ethereum: standard compliance and beyond](https://link.springer.com/article/10.1007/s41060-021-00281-1)

Review of a comprehensive method for detecting and classifying Ethereum token contracts, focusing on both ERC-compliant and non-compliant tokens. The approach involves several key techniques:

### Skeletons Creation: 
By analyzing contract bytecodes, the article identifies functional similarities between contracts.

### Sectioning EVM Bytecode: 
This involves decomposing contract bytecode into distinct sections like code, data, and metadata for better analysis.

### Extracting Function and Event Signatures: 
This crucial step identifies function and event signatures from the bytecode, which is essential for understanding a contract's interface. To extract function and event signatures from Ethereum token contracts, the authors employ a process that involves analyzing the contract's bytecode. They use a specific part of the Ethereum Virtual Machine (EVM) bytecode, known as the 'selector', which is a 4-byte hash. This selector is derived from the first four bytes of the Keccak-256 hash of the canonical representation of the function signature. By extracting and analyzing these selectors from the bytecode, the authors are able to identify the functions and events defined in the contract. This method allows them to systematically categorize and understand the contract's capabilities and compliance with Ethereum token standards​

### Header Restoration: 
The process aims to recover original function and event headers from bytecode signatures, using a comprehensive database of known headers and signatures. For the header restoration process, the authors utilize a database called [4byte.directory](https://www.4byte.directory/). This database contains a comprehensive collection of known function and event headers along with their respective 4-byte signatures. By matching the extracted signatures from the Ethereum contract bytecode with the signatures in this database, the authors are able to restore the original function and event headers. This method is crucial for understanding the contract's interface and determining its compliance with accepted Ethereum token standards​.

### Indicator-Based Analysis: 
Several indicators are used to identify non-compliant tokens. These indicators are based on aspects like ERC-20 signatures, contract names, and transfer events.
- **ERC-20 Signatures**: The presence or absence of specific ERC-20 signatures in a contract's bytecode is a primary indicator. ERC-20 is a widely accepted standard for Ethereum tokens, and compliance with this standard requires implementing certain functions and events. By analyzing the bytecode for these specific signatures, the authors can determine if a token adheres to the ERC-20 standard.

- **Contract Names**: The naming of a contract can provide hints about its intended functionality and compliance. For example, a contract named with terms commonly associated with token standards might be expected to adhere to those standards.

- **Transfer Events**: The handling of transfer events is a key aspect of ERC-20 compliant tokens. These events are emitted during token transfers and are essential for tracking token movements on the blockchain. The way a contract implements these events can indicate its compliance with the ERC-20 standard.