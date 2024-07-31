#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_PRODUCTS 100

typedef struct Product {
    char name[50];
    int price;
} Product;

void menu() {
    printf("\033[2J\033[H");
    printf("\033[1;36m⛽  WELCOME TO GAS STATION ⛽\033[0m\n");
    printf("Choose an action: \n");
    printf("[1] - Buy product\n");
    printf("[2] - Fill the fuel\n");
}

void buyProduct() {
    printf("\033[2J\033[H");
    printf("\033[1;36m⛽  OUR CONVENIENCE PRODUCTS ⛽\033[0m\n");

    Product products[] = {
        {"Potatle", 1},
        {"Orange", 2},
        {"Knife", 5},
        {"Banana", 1}
    };

    for(int i = 0; i < sizeof(products) / sizeof(products[0]); i++) {
        printf("[%d] - %s: $%d.00\n", i, products[i].name, products[i].price);
    }

    int choose;
    scanf("%d", &choose);
    getchar(); // clear buffer

    printf("You bought a %s\n", products[choose].name);

    printf("Press enter to back\n");
    getchar();
}

void fillTheFuel() {
    printf("\033[2J\033[H");
    printf("\033[1;36m⛽  FILLING THE GAS TANK ⛽\033[0m\n");

    printf("Costumer name: ");

    char name[50];
    scanf("%500s", &name);
    getchar(); // clear buffer

    printf("Hello %s, $50 dollars has been debited from your account\n", name);
    printf("Press enter to back\n");
    getchar();
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    while(1) {
        menu();
        
        char choose;
        choose = getchar();
        getchar(); // clear buffer

        switch (choose) {
            case '1':
                buyProduct();
                break;
            case '2':

            default:
                fillTheFuel();
                break;
        }
    }

    return 0;
}