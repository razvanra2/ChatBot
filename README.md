# Conversational AI for Reservation Placement
Group: Razvan Radoi, Bogdan Radulescu, Vlad Neculae.

## Problem Statement
One of the most advanced pieces of software is represented by conversational AIs. With a long-standing fasciation for machine dialogue and clear convenience brought to the table, conversational AIs have become increasingly popular. With modern day software, in fact, they are a hot commodity. 
A key feature of these conversational AIs is task-oriented dialogue: A feature that lets the user place orders or make reservations through speech.
Thus, the need for domain-specific chatbots arises: a series of task-focused chat bots that is able to interact with users through human-like speech that help them with completing tasks like reservations or order placements.

## Deliverables
The deliverables of this project are as follows:
1. A trained model of a chatbot that interacts with a subset of MultiWOZ that contains single-domain dialogues focused around restaurants reservations
2. An adjusted subset of MultiWOZ that is altered for RASA 2.X, 3.X and beyond input
3. A simple API for interacting with the restaurants database through RASA Actions
4. Config files needed for local RASA deployment and full interaction

## Set-up Steps
Requirements: Python 3.7 (3.8 and beyond not supported as of now for re-training due to current spacy limitations)

1. Clone this repository
2. Install RASA X
```
pip install rasa-x -i https://pypi.rasa.com/simple
```
3. In a terminal run:
```
rasa run actions
```

4. In a second terminal, run:
```
rasa shell
```
5. You may now interact with the chatbot from the second terminal, through the rasa shell

![Rasa Example](https://github.com/razvanra2/ChatBot/blob/master/ChatBotSample.png)

## References
* Bocklisch, T., Faulkner, J., Pawlowski, N., & Nichol, A. (2017). Rasa: Open source language understanding and dialogue management. arXiv preprint arXiv:1712.05181.

* Eric, M., Goel, R., Paul, S., Sethi, A., Agarwal, S., Gao, S., & Hakkani-Tur, D. (2019). Multiwoz 2.1: Multi-domain dialogue state corrections and state tracking baselines. arXiv preprint arXiv:1907.01669.

* Bursztyn V., Kohli V. (2020). CS 496 - Rasa Deployments.
