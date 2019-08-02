# Privacy-Preserving-Data-Mining

# # Abstract
This project deals with the question “Why we need to preserve data?” and basic Privacy Preserving Data Mining (PPDM) techniques. Data bearers such as hospitals, banks etc. have a vast amount of privately held data which is individual-specific. The main motive of these institutions is to release this privately held data to the general public or to the researchers in a way such that it is useful to them and also the privacy of those specific individuals is preserved.
Data owners want their highly sensitive data to be privacy preserved and protected so that they can easily share their data with anyone and at any time. The various techniques used like K-Anonymity, L-Diversity have their limitations. This project deals with the advantages and disadvantages of these techniques and the future scope of privacy preservation taking into consideration that no compromise is made with the privacy and confidentiality of data.
The most typical application of PPDM techniques is in the health care sector. In this project we have implemented the techniques on the given dataset of health care. Our aim is to seek novel solutions to the well-known trade-off between privacy and utility and to ensure personalized privacy solutions. In future we will be dealing with the further enhancements possible in this field including cryptography.





# # Privacy Preserving Data Mining (PPDM):
Privacy Preserving Data Mining is basically the data mining techniques used for preserving the sensitive data by not sacrificing the utility of data. The majority of PPDM techniques either modify the data or remove some of the original data to preserve the privacy. The data degradation between the privacy level and data quality is known as utility. Its basic aim is to build algorithms for the above purpose by transforming the data in some form or the other.
Due to the advancement in various technologies, ubiquitous and pervasive computing is generating large amounts of information. Various fields like health care, banking, cyber security, transportation and many other contains data that needs to be preserved. For e.g. medical records in any e-healthcare field - violation of the private information of a patient like name, disease he is suffering from, its treatment etc. is very sensitive and need not be shared with anyone, and therefore, to fulfill this purpose of sensitive data protection, these techniques are used. It is also used in various other domains in a similar way. Most of the PPDM algorithms either modify the data or simply remove it while sharing its database. Sometimes losing the data leads to various other issues. Hence our project deals with all such aspects of the algorithm – their implementation, present scenario of the algorithms, pros and cons of each methodology, their advancement and future scope in this field of research.




# # K- Anonymity
An identifier is a certain property or characteristic that is used to describe an individual. It may or may not be same for two different individuals. For example, Name, Age, Gender, Date of Birth are some commonly used identifiers.
Quasi-identifiers [2] are those identifiers which are themselves not unique identifiers but when combined with other quasi-identifiers can become a source of identity information. This is called re-identification through the use of quasi-identifiers. For example, neither of these identifiers such as gender, date of birth or postal codes can single-handedly identify an individual. But when these 3 identifiers are combined they can very easily identify more than half of the population. This is a case of re-identification by linking various available datasets scattered across the web. K-Anonymity[2] is a property of a dataset used to describe the dataset’s level of anonymity. If the person’s information in a given dataset cannot be distinguished from at least (k-1) person’s information in the same dataset then the dataset is said to be K-anonymous. Some of the techniques [2] used in the implementation of k-anonymity are:

# Generalization

It is a technique in which a value of a particular attribute is replaced by a more general and less specific value which is consistent with the original dataset. 

# Suppression

Suppression is a method of removal of specific information from the dataset to protect the identity and privacy of an individual. In this method all or some values of the attributes are replaced by asterisk ‘*’.The set of k records is known as equivalence class. Any record in a k anonymized data set has a maximum probability 1/k of being re-identified known as the threshold risk. Higher values of k implies a lower probability of re-identification, but also more distortion to the data, and hence greater information loss due to k anonymization. Excessive anonymization can make the disclosed data less useful to the recipients because it produces biased and incorrect results.
So the main advantage of K anonymity is that to an extent it helps in providing privacy to an individual by using generalisation and suppression techniques to remove the straightforward identifiers that can cause serious threat to a person’s privacy. Also it has one more advantage i.e. it is easy and simple to understand and implement.


# # Attacks on K-Anonymity:

Homogeneity Attack: This attack generally occurs due to the lack of diversity of sensitive attributes in a generalized group that can lead to an unintentional disclosure to someone who knows some very basic information of an individual. So, the aim of privacy is not fulfilled.
Background-knowledge Attack: By knowing the certain background knowledge one can successfully eliminate possible values of sensitive attributes of an individual with very high probability and can get to know the sensitive data.

# # Limitations:
Removing only some of the obvious identifiers doesn’t help as the remaining set of identifiers, known as quasi identifiers can combine together and use the available dataset to re- identify a particular individual.
Also, as K increases the level of anonymity increases but the information loss also increases as the values of the attributes or the identifiers keeps on decreasing. So there is heavy distortion of data with increase in the value of k or the level of anonymity. Also, it does not take into consideration the sensitive attributes for anonymization which can disclose information.
