use std::io::{self, Write};

fn main() {
    loop {
        print!("$ ");
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        let trimmed_input = input.trim();

        if trimmed_input.is_empty() {
            continue;
        } else if trimmed_input == "exit" {
            break;
        } else {
            println!("Unknown command: {}", trimmed_input);
        }
    }

    println!("Exiting shell");
}

