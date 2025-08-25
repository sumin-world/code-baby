use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read, Write};

fn main() {
    // 입력 전체 읽기
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();
    let mut heap = BinaryHeap::new();

    let mut output = String::new(); // 출력 버퍼

    for _ in 0..n {
        let x: i32 = iter.next().unwrap().parse().unwrap();
        if x == 0 {
            if let Some(Reverse(min_val)) = heap.pop() {
                output.push_str(&format!("{}\n", min_val));
            } else {
                output.push_str("0\n");
            }
        } else {
            heap.push(Reverse(x));
        }
    }

    // 최종 출력
    let mut stdout = io::BufWriter::new(io::stdout());
    stdout.write_all(output.as_bytes()).unwrap();
}
