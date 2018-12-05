#ifndef AJOUT_BENEVOLES_H
#define AJOUT_BENEVOLES_H

#include <QDialog>

namespace Ui {
class Ajout_Benevoles;
}

class Ajout_Benevoles : public QDialog
{
    Q_OBJECT

public:
    explicit Ajout_Benevoles(QWidget *parent = 0);
    ~Ajout_Benevoles();

private:
    Ui::Ajout_Benevoles *ui;
};

#endif // AJOUT_BENEVOLES_H
