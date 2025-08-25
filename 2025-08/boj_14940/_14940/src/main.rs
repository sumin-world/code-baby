use std::collections::VecDeque;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap(); // rows (세로)
    let m: usize = iter.next().unwrap().parse().unwrap(); // cols (가로)

    let mut grid = vec![vec![0i32; m]; n];
    let mut start = (0usize, 0usize);

    for i in 0..n {
        for j in 0..m {
            let v: i32 = iter.next().unwrap().parse().unwrap();
            grid[i][j] = v;
            if v == 2 {
                start = (i, j);
            }
        }
    }

    let dirs: [(i32, i32); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];
    let mut dist = vec![vec![-1i32; m]; n];
    let mut q: VecDeque<(usize, usize)> = VecDeque::new();

    dist[start.0][start.1] = 0;
    q.push_back(start);

    while let Some((x, y)) = q.pop_front() {
        for &(dx, dy) in &dirs {
            let nx = x as i32 + dx;
            let ny = y as i32 + dy;
            if nx >= 0 && nx < n as i32 && ny >= 0 && ny < m as i32 {
                let (ux, uy) = (nx as usize, ny as usize);
                if dist[ux][uy] == -1 && grid[ux][uy] != 0 {
                    dist[ux][uy] = dist[x][y] + 1;
                    q.push_back((ux, uy));
                }
            }
        }
    }

    for i in 0..n {
        for j in 0..m {
            if grid[i][j] == 0 {
                print!("0");
            } else {
                print!("{}", dist[i][j]);
            }
            if j + 1 < m {
                print!(" ");
            }
        }
        println!();
    }
}
