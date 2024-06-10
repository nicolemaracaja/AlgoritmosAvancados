#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// Definição do tamanho máximo do grafo
const ll N = 1000001;

// Lista de adjacência para representar o grafo
vector<ll> adj[N];

// Vetor para armazenar o tamanho dos caminhos mais longos
vector<ll> tamanho(N, -1);

// Função para realizar busca em profundidade (DFS) para encontrar o caminho mais longo
ll dfs(ll u) {
    // Se já calculamos o tamanho para esse vértice, retorna o valor
    if (tamanho[u] != -1)
        return tamanho[u];

    // Calcula o maior caminho a partir desse vértice
    ll tamMax = 0;
    for (auto e : adj[u]) {
        tamMax = max(tamMax, dfs(e));
    }

    // Armazena o resultado do tamanho do caminho mais longo
    tamanho[u] = 1 + tamMax;
    return tamanho[u];
}

int main() {
    ios::sync_with_stdio(0);  // Otimização para entrada/saída
    cin.tie(0);
    cout.tie(0);

    ll n, m, x, y;
    cin >> n >> m;  // Lê o número de vértices e arestas

    // Lê as arestas e preenche a lista de adjacência
    for (ll i = 0; i < m; i++) {
        cin >> x >> y;
        adj[x].push_back(y);  // Adiciona aresta direcionada
    }

    ll maior = 0;
    // Calcula o caminho mais longo a partir de cada vértice
    for (ll i = 1; i <= n; i++) {
        maior = max(maior, dfs(i));
    }

    // Imprime o comprimento do caminho mais longo
    cout << maior - 1 << endl;  // Menos 1 para contar apenas as arestas

    return 0;
}
