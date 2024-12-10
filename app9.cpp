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
    cout << "1. Add Member\n";
    cout << "2. Add President\n";
    cout << "3. Add Secretary\n";
    cout << "4. Delete Member\n";
    cout << "5. Display Members\n";
    cout << "6. Exit\n";
    cout << "Choose an option: ";
};

int main() {
    Club club;
    int choice;
    string name;
    int prn;

    do {
        displayMenu();
        cin >> choice;
        cout << "\n\n";
        switch (choice) {
        case 1:
            cout << "Enter name: ";
            cin >> name;
            cout << "Enter PRN: ";
            cin >> prn;
            club.addMember(name, prn);
            cout << "Member added.\n";
            break;

        case 2:
            cout << "Enter president's name: ";
            cin >> name;
            cout << "Enter president's PRN: ";
            cin >> prn;
            club.addPresident(name, prn);
            cout << "President added.\n";
            break;

        case 3:
            cout << "Enter secretary's name: ";
            cin >> name;
            cout << "Enter secretary's PRN: ";
            cin >> prn;
            club.addSecretary(name, prn);
            cout << "Secretary added.\n";
            break;

        case 4:
            cout << "Enter name of the member to delete: ";
            cin >> name;
            club.deleteMember(name);
            break;

        case 5:
            cout << "Club members: \n";
            club.displayMembers();
            cout << "Total club members: " << club.getTotalMember() << endl;
            break;

        case 6:
            cout << "Exiting...\n";
            break;

        default:
            cout << "Invalid choice! Please try again.\n";
        }
    } while (choice != 6);

    return 0;
}
