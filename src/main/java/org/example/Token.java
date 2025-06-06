package org.example;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@AllArgsConstructor
public class Token {
     TokenType type;
     String lexeme;
     Object literal;
     int line;

    @Override
    public String toString() {
        return "Token{" +
                "type:" + type +
                ", lexeme:'" + lexeme + '\'' +
                ", literal:" + literal +
                ", line:" + line +
                '}';
    }
}
