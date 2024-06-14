function solution(info, edges) {
    const graph = Array.from(Array(info.length), () => []);
    edges.forEach((edge) => {
        const [parent, child] = edge;
        graph[parent].push(child);
    });
    
    return dfs(0, [], [0, 0], info, graph);
}

function dfs(now, nexts, cnt, info, graph) {
    cnt[info[now]]++;
    if (cnt[1] >= cnt[0]) return;
    
    let answer = cnt[0];
    nexts = [...nexts, ...graph[now]];
    nexts.forEach((next, ind) => {
        const newNexts = [...nexts.slice(0, ind), ...nexts.slice(ind + 1)];
        const temp = dfs(next, newNexts, [...cnt], info, graph);
        if (temp > answer) answer = temp;
    });
    
    return answer;
}