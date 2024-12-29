package org.example;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@AllArgsConstructor
public class Token {
    //vazhe
    private TokenType type;
    private String lexeme;
    private Object literal;
    private int line;

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
