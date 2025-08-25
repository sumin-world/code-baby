use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();
    let mut stack = Vec::new();
    let mut results = Vec::new();

    for _ in 0..n {
        let command = iter.next().unwrap();

        match command {
            "push" => {
                let x: i32 = iter.next().unwrap().parse().unwrap();
                stack.push(x);
            },
            "pop" => {
                if let Some(item) = stack.pop() {
                    results.push(item.to_string());
                } else {
                    results.push("-1".to_string());
                }
            },
            "size" => {
                results.push(stack.len().to_string());
            },
            "empty" => {
                let result = if stack.is_empty() { "1" } else { "0" };
                results.push(result.to_string());
            },
            "top" => {
                if let Some(&item) = stack.last() {
                    results.push(item.to_string());
                } else {
                    results.push("-1".to_string());
                }
            },
            _ => {}
        }
    }

    println!("{}", results.join("\n"));
}