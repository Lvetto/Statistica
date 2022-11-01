#include <iostream>
#include <cmath>
#include <fstream>

#include <TApplication.h>
#include <TCanvas.h>
#include <TPad.h>
#include <TH1F.h>
#include <TGraph.h>

using namespace std;

double max(double* array, int len) {
    double out = array[0];
    for (int i=1; i<len; i++) {
        if (array[i] > out) {
            out = array[i];
        }
    }
    return out;
}

double min(double* array, int len) {
    double out = array[0];
    for (int i=1; i<len; i++) {
        if (array[i] < out) {
            out = array[i];
        }
    }
    return out;
}

int main(int argc, char* argv[]) {
    if (argc < 4) {
        cout << "Usage: program <file name> <lenght> <bins>" << endl;
        return -1;
    }

    fstream file;
    file.open(argv[1], ios::in);

    int len = atoi(argv[2]);
    double* data = new double[len];
    for (int i=0; i<len; i++) {
        file >> data[i];
    }

    TApplication app("app", 0, 0);

    TCanvas* c = new TCanvas(argv[1], argv[1], 1000, 500);
    TPad* p1 = new TPad("name", "Istogramma", 0, 0, 1, 1);
    p1->Draw();
    p1->cd();

    TH1F* h = new TH1F("Distribuzione", argv[1], atoi(argv[3]), min(data, len), max(data, len));
    for (int i=0; i<len; i++) {
        h->Fill(data[i]);
    }
    h->Draw();
    c->Update();
    c->Draw();
    app.Run();

    return 0;
}