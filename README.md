# de-id

With the volume and availability of data in today’s world, big data programs are becoming more widely adopted and empowering organisations and governments with valuable insights. On the back of this new technology adoption is the responsibility of organisations to ensure an individual’s right to privacy is upheld, particularly in cases where there is sensitive information present. One such approach to preserving an individual’s personal privacy is applying the principle of ‘K-Anonymity’ in vulnerable data sets.

A practical solution is proposed using the ‘Apache Hadoop’ big data framework and Python programming to create a control layer around the Hadoop processing environment. The control layer will check for sensitive information and apply de-identification techniques to data sets where required. This ensures all data sets are in a state of K-Anonymity when being accessed.

![Figure 1 - de-identification control layer](https://github.com/milhou5/de-id/blob/master/Figure1_de-id-control.png)

By appending the de-identification script at each endpoint of the big data system, a control layer is created that can protect the privacy of individuals with records contained in the Hadoop database. The Python program will analyse a data set and classify the attributes according to their sensitivity and identifying qualities. Upon classification the generalisation and suppression techniques are applied to the data until the data set has been de-identified and k-anonymity achieved.

In the solution proposed, the control layer (see figure 1) serves three primary functions. 

1. The first is to identify activity associated with data sets that contain sensitive information. Any activities that are identified as including sensitive personal information are logged and available for review and auditing.

1. The second purpose is to provide a functional capability to de-identify any data sets using the principle of K-Anonymity. By identifying and classifying attributes, and applying the generalisation and suppression techniques where appropriate, the risk of privacy breach is reduced within an organisation.

1. The third function is arguably the most important. With the user-focussed design and interactive nature of the de-identification script, it creates and reinforces awareness of the sensitivity of data and the importance of maintaining an individual’s right to privacy.

It must also be considered that without the implementation of appropriate database access and audit controls provided by the Hadoop framework (Revathy and Srinivasan, 2018), the proposed solution becomes ineffective. Without these additional security controls, users can easily bypass the de-identification layer without detection. It is intended to be used in conjunction with the ‘Secure Mode’ feature provided by Apache Hadoop, as well as more standard organisational controls like multi-factor authentication, data encryption and network security hygiene.

