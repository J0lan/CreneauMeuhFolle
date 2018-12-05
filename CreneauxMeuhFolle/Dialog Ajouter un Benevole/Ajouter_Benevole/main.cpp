#include "ajout_benevole.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Ajout_Benevoles w;
    w.show();

    return a.exec();
}
