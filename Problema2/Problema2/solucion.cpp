#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <chrono>
#include <fstream>
#include <iomanip>

using namespace std;
using namespace std::chrono;

// Función para generar coeficientes usando el triángulo de Pascal
vector<long long> generarCoeficientesPascal(int n) {
    vector<long long> coeficientes;
    
    if (n == 0) {
        coeficientes.push_back(1);
        return coeficientes;
    }
    
    // Inicializar con la primera fila
    coeficientes.push_back(1);
    
    for (int i = 1; i <= n; i++) {
        vector<long long> nuevoCoeficiente;
        nuevoCoeficiente.push_back(1); // Primer coeficiente siempre es 1
        
        // Calcular coeficientes intermedios
        for (int j = 1; j < i; j++) {
            nuevoCoeficiente.push_back(coeficientes[j - 1] + coeficientes[j]);
        }
        
        nuevoCoeficiente.push_back(1); // Último coeficiente siempre es 1
        coeficientes = nuevoCoeficiente;
    }
    
    return coeficientes;
}

// Función para mostrar el polinomio en formato legible
string mostrarPolinomio(const vector<long long>& coeficientes) {
    int n = coeficientes.size() - 1;
    string polinomio = "";
    
    for (int i = 0; i < coeficientes.size(); i++) {
        int exponente = n - i;
        long long coef = coeficientes[i];
        
        if (coef == 0) continue;
        
        if (i > 0) polinomio += " + ";
        
        if (exponente == 0) {
            polinomio += to_string(coef);
        } else if (exponente == 1) {
            if (coef == 1) {
                polinomio += "x";
            } else {
                polinomio += to_string(coef) + "x";
            }
        } else {
            if (coef == 1) {
                polinomio += "x^" + to_string(exponente);
            } else {
                polinomio += to_string(coef) + "x^" + to_string(exponente);
            }
        }
    }
    
    return polinomio;
}

// Función para calcular el polinomio mostrando pasos
double calcularPolinomioPasos(const vector<long long>& coeficientes, double x) {
    int n = coeficientes.size() - 1;
    double resultado = 0.0;
    
    cout << "\nCálculo paso a paso para x = " << x << ":" << endl;
    cout << "Polinomio: " << mostrarPolinomio(coeficientes) << endl;
    cout << string(50, '-') << endl;
    
    for (int i = 0; i < coeficientes.size(); i++) {
        int exponente = n - i;
        long long coef = coeficientes[i];
        double termino = coef * pow(x, exponente);
        resultado += termino;
        
        if (exponente == 0) {
            cout << "Término " << (i + 1) << ": " << coef << " × " 
                 << x << "^" << exponente << " = " << coef << " × 1 = " << termino << endl;
        } else {
            cout << "Término " << (i + 1) << ": " << coef << " × " 
                 << x << "^" << exponente << " = " << coef << " × " 
                 << pow(x, exponente) << " = " << termino << endl;
        }
    }
    
    cout << string(50, '-') << endl;
    cout << "Resultado final: " << resultado << endl;
    cout << "Verificación: (" << x << " + 1)^" << n << " = " << resultado << endl;
    
    return resultado;
}

int main() {
    try {
        int n;
        cout << "Ingrese el valor de n (entero no negativo): ";
        cin >> n;
        
        if (n < 0) {
            cout << "Error: n debe ser un número entero no negativo" << endl;
            return 1;
        }
        
        // Medir tiempo de generación de coeficientes
        auto inicioGeneracion = high_resolution_clock::now();
        vector<long long> coeficientes = generarCoeficientesPascal(n);
        auto finGeneracion = high_resolution_clock::now();
        auto duracionGeneracion = duration_cast<microseconds>(finGeneracion - inicioGeneracion);
        
        cout << "\n=== RESULTADOS PARA n = " << n << " ===" << endl;
        cout << "Coeficientes: ";
        for (size_t i = 0; i < coeficientes.size(); i++) {
            cout << coeficientes[i];
            if (i < coeficientes.size() - 1) cout << " ";
        }
        cout << endl;
        cout << "Polinomio: " << mostrarPolinomio(coeficientes) << endl;
        cout << "Tiempo de generación: " << duracionGeneracion.count() / 1000000.0 << " segundos" << endl;
        
        // Calcular para un valor específico de x
        double x;
        cout << "\nIngrese el valor de x para calcular el polinomio: ";
        cin >> x;
        
        auto inicioCalculo = high_resolution_clock::now();
        double resultado = calcularPolinomioPasos(coeficientes, x);
        auto finCalculo = high_resolution_clock::now();
        auto duracionCalculo = duration_cast<microseconds>(finCalculo - inicioCalculo);
        
        cout << "Tiempo de cálculo: " << duracionCalculo.count() / 1000000.0 << " segundos" << endl;
        
        // Guardar resultados en archivo
        string nombreArchivo = "resultados_polinomio_n" + to_string(n) + ".txt";
        ofstream archivo(nombreArchivo);
        
        if (archivo.is_open()) {
            archivo << "RESULTADOS PARA (x+1)^" << n << endl;
            archivo << string(50, '=') << endl;
            archivo << "Coeficientes: ";
            for (size_t i = 0; i < coeficientes.size(); i++) {
                archivo << coeficientes[i];
                if (i < coeficientes.size() - 1) archivo << " ";
            }
            archivo << endl;
            archivo << "Polinomio: " << mostrarPolinomio(coeficientes) << endl;
            archivo << "Tiempo de generación: " << fixed << setprecision(6) 
                   << duracionGeneracion.count() / 1000000.0 << " segundos" << endl;
            archivo << "Valor calculado para x=" << x << ": " << resultado << endl;
            archivo << "Tiempo de cálculo: " << fixed << setprecision(6) 
                   << duracionCalculo.count() / 1000000.0 << " segundos" << endl;
            
            archivo.close();
            cout << "\nResultados guardados en '" << nombreArchivo << "'" << endl;
        } else {
            cout << "Error: No se pudo abrir el archivo para escribir" << endl;
        }
        
        // Prueba específica para n=100
        if (n == 100) {
            cout << "\n=== PRUEBA ESPECÍFICA PARA n=100 ===" << endl;
            cout << "Número de coeficientes: " << coeficientes.size() << endl;
            
            long long maxCoef = 0;
            for (long long coef : coeficientes) {
                if (coef > maxCoef) maxCoef = coef;
            }
            cout << "Coeficiente máximo: " << maxCoef << endl;
        }
        
    } catch (const exception& e) {
        cout << "Error inesperado: " << e.what() << endl;
        return 1;
    }
    
    return 0;
}