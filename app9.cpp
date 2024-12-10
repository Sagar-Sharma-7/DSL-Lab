// linked list

// the department of computer engineering ha student's club named 'pinnacle club'. Students of second, third and final year of department can be granted membership on request. Similarly one may cancel the membership of club. First node is reserved for president of club and last node is reserved for secretary of club. Write c++ program to maintain club member's information using singly lined list. Sotre student PRN and Name. Write functions to
// a) add the members as well as president or even secretary.
// b) compute total number of members of club.
// c) display members
// d) two linked list exist for two divisions

#include <bits/stdc++.h>
using namespace std;

class Node {
    string name;
    int PRN;
    Node* next;
public:
    Node(string name, int prn) {
        this->name = name;
        this->PRN = prn;
        this->next = nullptr;
    }

    int getPRN() {
        return PRN;
    }

    void setPRN(int prn) {
        PRN = prn;
    }

    string getName() {
        return name;
    }

    void setName(string name) {
        this->name = name;
    }

    Node* getNext() {
        return next;
    }

    void setNext(Node* nextNode) {
        next = nextNode;
    }
};

class Club {
private:
    Node* head;
    Node* tail;
    int count;
public:
    Club() {
        head = nullptr;
        tail = nullptr;
        count = 0;
    }

    // Function to add a new member
    void addMember(string name, int prn) {
        Node* newNode = new Node(name, prn);
        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            tail->setNext(newNode);
            tail = newNode;
        }
        count++;
    }

    // Function to add the president
    void addPresident(string name, int prn) {
        Node* newNode = new Node(name, prn);
        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            newNode->setNext(head);
            head = newNode;
        }
        count++;
    }

    // Function to add the secretary
    void addSecretary(string name, int prn) {
        Node* newNode = new Node(name, prn);
        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            tail->setNext(newNode);
            tail = newNode;
        }
        count++;
    }

    // Function to delete a member by their name
    void deleteMember(string name) {
        Node* current = head;
        Node* prev = nullptr;

        // If the head node itself is the member to be deleted
        if (current != nullptr && current->getName() == name) {
            head = current->getNext(); // Change head
            delete current;
            count--;
            cout << name << " has been removed from the club.\n";
            return;
        }

        // Search for the member to be deleted
        while (current != nullptr && current->getName() != name) {
            prev = current;
            current = current->getNext();
        }

        // If the member was not found
        if (current == nullptr) {
            cout << name << " not found in the club.\n";
            return;
        }

        // Unlink the node from the linked list
        prev->setNext(current->getNext());
        delete current;
        count--;
        cout << name << " has been removed from the club.\n";
    }

    // Function to display all members
    void displayMembers() {
        Node* current = head;
        while (current) {
            cout << "Name: " << current->getName() << ", PRN: " << current->getPRN() << '\n';
            current = current->getNext();
        }
    }

    // Function to get the total number of members
    int getTotalMember() {
        return count;
    }
};

// Function to display the menu
void displayMenu() {
    cout << "Menu:\n";
    cout << "1. Create New Division\n";
    cout << "2. Add Member\n";
    cout << "3. Add President\n";
    cout << "4. Add Secretary\n";
    cout << "5. Delete Member\n";
    cout << "6. Display Members\n";
    cout << "7. Exit\n";
    cout << "Choose an option: ";
};

int main() {
    map<int, Club> divisions;
    int choice, divisionID;
    string name;
    int prn;

    do {
        displayMenu();
        cin >> choice;
        cout << "\n\n";
        switch (choice) {
        case 1:
            cout << "Enter new Division ID: " << endl;
            cin >> divisionID;
            if (divisions.find(divisionID) == divisions.end()) {
                divisions[divisionID] = Club();
                cout << "New division " << divisionID << " created.\n";
            } else {
                cout << "DivisionID already exists.\n";
            }
            cout << "\n\n";
            break;

        case 2:
            cout << "Enter division ID: ";
            cin >> divisionID;
            if (divisions.find(divisionID) != divisions.end()) {
                cout << "Enter name: ";
                cin >> name;
                cout << "Enter PRN: ";
                cin >> prn;
                divisions[divisionID].addMember(name, prn);
            } else {
                cout << "Division ID does not exist.\n";
            }
            cout << "\n\n";
            break;

        case 3:
            cout << "Enter division ID: ";
            cin >> divisionID;
            if (divisions.find(divisionID) != divisions.end()) {
                cout << "Enter new president's name: ";
                cin >> name;
                cout << "Enter new president's PRN: ";
                cin >> prn;
                divisions[divisionID].addPresident(name, prn);
            } else {
                cout << "Division ID does not exist.\n";
            }
            cout << "\n\n";
            break;

        case 4:
            cout << "Enter division ID: ";
            cin >> divisionID;
            if (divisions.find(divisionID) != divisions.end()) {
                cout << "Enter new secretary's name: ";
                cin >> name;
                cout << "Enter new secretary's PRN: ";
                cin >> prn;
                divisions[divisionID].addSecretary(name, prn);
            } else {
                cout << "Division ID does not exist.\n";
            }
            cout << "\n\n";
            break;

        case 5:
            cout << "Enter division ID: ";
            cin >> divisionID;
            if (divisions.find(divisionID) != divisions.end()) {
                cout << "Enter name of the member to delete: ";
                cin >> name;
                divisions[divisionID].deleteMember(name);
            } else {
                cout << "Division ID does not exist.\n";
            }
            cout << "\n\n";
            break;

        case 6:
            cout << "Enter division ID: ";
            cin >> divisionID;
            if (divisions.find(divisionID) != divisions.end()) {
                cout << "Division " << divisionID << " members: " << endl;
                divisions[divisionID].displayMembers();
                cout << "Total club members of Division " << divisionID << ": " << divisions[divisionID].getTotalMember() << endl;
            } else {
                cout << "Division ID does not exist.\n";
            }
            cout << "\n\n";
            break;

        case 7:
            cout << "Exiting...\n";
            break;

        default:
            cout << "Invalid choice! Please try again.\n";
        }
    } while (choice != 7);

    return 0;
}

