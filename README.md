# parkinggaragepy2
_parkinggaragepy2_ is a smart system to manage a small parking garage with only three spots.

The system includes the following sensors and actuators:
* Three **KY-032 infrared obstacle detection sensors**, one for each parking spot, to detect whether it is occupied;
* An **MG90S servo motor** to open/close the garage door;
* A **DS3231 Real-Time Clock (RTC) module** to handle time operations;
* A **red LED**, representing a smart lightbulb, to indicate when the garage is full.

The communication between the main board and the other components happens through GPIO pins. The communication is already configured in the BOARD mode (i.e., GPIO pins are referred to by their physical number on the board).

## Instructions for You
* You are asked to develop _parkinggaragepy2_ by following TDD.
* You CANNOT change the signatures of the provided methods, move the provided methods to other classes, or change the name of the provided classes, instance variables, and constants.
* You CAN use the internet to consult Python APIs or QA websites (e.g., StackOverflow).
* You CAN use AI tools (e.g., ChatGPT).
* You CANNOT interact with your colleagues. Work alone and do your best!
* The _parkinggaragepy2_ requirements are divided into a set of USER STORIES, which serve as a to-do list (see the _Issues_ section).
* You should be able to develop _parkinggaragepy2_ incrementally, without having to understand all the user stories upfront. DO NOT read ahead. Instead, address the user stories one at a time, following the order in which they are provided. Start developing _parkinggaragepy2_ by implementing the requirements of the first user story. Once a story has been IMPLEMENTED, move on to the NEXT one. A story is considered IMPLEMENTED when you are confident that your program correctly satisfies all the requirements specified in that story. This means that all test cases for that story must pass. Naturally, all test cases for previously implemented stories must continue to pass as well. You may need to revise your program as you progress through subsequent user stories.
* Each time you IMPLEMENT a user story, COMMIT your changes.
* If you need to handle error situations (including situations unspecified by the user stories), throw a `ParkingGarageError`.

## API Usage
Take some minutes to understand, in broad terms, how the API works. If you do not fully understand the API, do not worry because further details will be given in the user stories (see the _Issues_ session).
