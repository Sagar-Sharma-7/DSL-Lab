// linked list

// the department of computer engineering ha student's club named 'pinnacle club'. Students of second, third and final year of department can be granted membership on request. Similarly one may cancel the membership of club. First node is reserved for president of club and last node is reserved for secretary of club. Write c++ program to maintain club member's information using singly lined list. Sotre student PRN and Name. Write functions to
// a) add the members as well as president or even secretary.
// b) compute total number of members of club.
// c) display members
// d) two linked list exist for two divisions

#include <bits/stdc++.h>
using namespace std;

class Node{
    string name;
    int PRN;
    Node* next;
    public:
        Node(string name, int prn){
            this->name = name;
            this->PRN = prn;
            this->next = nullptr;
        };

        int getPRN(){
            return PRN;
        }

        int setPRN(int prn){
            PRN = prn;
        }

        string getName(){
            return name;
        }

        string setName(string name){
            this->name = name;
        }

        Node* getNext(){
            return next;
        }

        Node* setNext(Node* nextNode){
            next = nextNode;
        }
};

class Club{
    private:
        Node* head;
        Node* tail;
        int count;
    public:
        Club(){
            head = nullptr;
            tail = nullptr;
            count = 0;
        };

        void addMember(string name, int prn){
            Node* newNode = new Node(name, prn);
            if(head == nullptr){
                head = newNode;
                tail = newNode;
            }else{
                tail->setNext(newNode);
                tail = newNode;
            }
            count++;
        }

        void addPresident(string name, int prn){
            Node* newNode = new Node(name, prn);
            if(head == nullptr){
                head = newNode;
                tail = newNode;
            }else{
                newNode->setNext(head);
                head = newNode;
            }
            count++;
        }

        void addSecretary(string name, int prn){
            Node* newNode = new Node(name, prn);
            if(head == nullptr){
                head = newNode;
                tail = newNode;
            }else{
                tail->setNext(newNode);
                tail = newNode;
            }
            count++;
        }

        void displayMembers(){
            Node* current = head;
            while(current){
                cout << "Name: " << current->getName() << ", PRN: " << current->getPRN() << '\n';
                current = current->getNext();
            }
        }

        int getTotalMember(){
            return count;
        }
};

void displayMenu(){
    cout << "Menu:\n";
    cout << "1. Create New Division\n";
    cout << "2. Add Member\n";
    cout << "3. Add President\n";
    cout << "4. ADD Secretary\n";
    cout << "5. Display Members\n";
    cout << "6. Exit\n";
    cout << "Choose an option: ";
};

int main(){
    map<int, Club> divisions;
    int choice, divisionID;
    string name;
    int prn;

    do{
        displayMenu();
        cin >> choice;
        cout << "\n\n";
        switch(choice){
            case 1: 
                cout << "Enter new Division ID: " << endl;
                cin >> divisionID;
                if(divisions.find(divisionID) == divisions.end()){
                    divisions[divisionID] = Club();
                    cout << "New division " << divisionID << " created.\n";
                }else {
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
                    cout << "Enter new secreatary's PRN: ";
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
                    cout << "Division " << divisionID << " members: " << endl;
                    divisions[divisionID].displayMembers();
                    cout << "Total club members of Division " << divisionID << ": " << divisions[divisionID].getTotalMember() << endl;
                } else {
                    cout << "Division ID does not exist.\n";
                }
                cout << "\n\n";
                break;

            case 6:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
    } while (choice != 6);


    // Club d1;
    // Club d2;

    // d1.addPresident("Vansh", 101);
    // d1.addMember("swarup", 56);
    // d1.addMember("sagar", 48);
    // d1.addMember("raghav", 42);
    // d1.addSecretary("kaushal", 201);

    // d2.addPresident("harsh", 301);
    // d2.addMember("aarav", 2);
    // d2.addMember("daksh", 13);
    // d2.addMember("ayush", 17);
    // d2.addSecretary("deepshika", 22);

    // cout << "Division 1 members: " << endl;
    // d1.displayMembers();
    // cout << "Total club members of Division 1 is : " << d1.getTotalMember() << endl;
    // cout << " " << endl;

    // cout << "Division 2 members: " << endl;
    // d2.displayMembers();
    // cout << "Total club members of Division 2 is : " << d2.getTotalMember() << endl;
    // cout << " " << endl;


    return 0;
}
