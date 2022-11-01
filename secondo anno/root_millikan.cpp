#include <iostream>
#include <cmath>
#include <math.h>
#include <fstream>

#include <TApplication.h>
#include <TCanvas.h>
#include <TPad.h>
#include <TH1F.h>
#include <TGraph.h>

using namespace std;

int main(int argc, char* argv[]) {
    if (argc < 4) {
        cout << "Usage: program <file name> <lenght> <steps>" << endl;
        return -1;
    }

    int len = atoi(argv[2]);

    fstream file;
    file.open(argv[1], ios::in);

    double* data = new double[len];
    for (int i=0; i<len; i++) {
        file >> data[i];
    }

    TApplication app("app", 0, 0);

    TCanvas* c = new TCanvas(argv[1], argv[1], 1000, 500);
    TPad* p1 = new TPad("name", "Istogramma", 0, 0, 1, 1);
    p1->Draw();
    p1->cd();

    int steps = atoi(argv[3]);
    double* xs = new double[steps];
    double* ys = new double[steps];
    for (int i=0; i<steps+1; i++) {
        double q = 1.5E-19 + (i * (0.2E-19/steps));
        xs[i] = q;
        ys[i] = 0;
        for (int j=0; j<len; j++) {
            double Q = data[i];
            double k;
            modf(Q/q + 0.5, &k);
            ys[i] += pow((Q/k) - q, 2);
        }
        cout << xs[i] << " " << ys[i] << endl;
    }


    TGraph* g = new TGraph(len, xs, ys);
    g->Draw();
    c->Update();
    c->Draw();
    app.Run();

    return 0;
}