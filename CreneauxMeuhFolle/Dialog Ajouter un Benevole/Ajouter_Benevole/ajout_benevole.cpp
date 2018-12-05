#include "ajout_benevole.h"
#include "ui_ajout_benevoles.h"

Ajout_Benevoles::Ajout_Benevoles(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Ajout_Benevoles)
{
    ui->setupUi(this);
}

Ajout_Benevoles::~Ajout_Benevoles()
{
    delete ui;
}
