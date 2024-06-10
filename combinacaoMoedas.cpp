#include <iostream>
#include <vector>
#define MOD 1000000007

using namespace std;

// Função para calcular o número de maneiras de formar a soma X usando as moedas
int count_ways(int n, int x, const vector<int>& coins) {
    // Inicialize o vetor dp com zero
    vector<int> dp(x + 1, 0);
    // Há uma maneira de formar a soma 0 (sem usar moedas)
    dp[0] = 1;

    // Para cada soma de 1 a x
    for (int i = 1; i <= x; i++) {
        // Para cada moeda disponível
        for (int j = 0; j < n; j++) {
            if (i >= coins[j]) {
                // Se a moeda pode ser usada para formar a soma
                dp[i] = (dp[i] + dp[i - coins[j]]) % MOD;
            }
        }
    }

    return dp[x];
}

int main() {
    // Leitura dos valores de entrada
    int n, x;
    cin >> n >> x;
    vector<int> coins(n);

    // Leitura dos valores das moedas
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    // Cálculo do número de maneiras de formar a soma x
    cout << count_ways(n, x, coins) << endl;

    return 0;
}
