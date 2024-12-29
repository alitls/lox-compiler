package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ScannerTest {

    @Test
    void test() {
        System.out.println("\n\n");
        String source = "( ";
        Scanner scanner = new Scanner(source);
        scanner.scanTokens();
        scanner.print();
        System.out.println("\n\n");
    }
}