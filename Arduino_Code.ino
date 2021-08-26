#include "HX711.h"
#define CLK A0 // clock pin to the load cell amp
#define DOUT1 A1 // data pin to the first lca
#define DOUT2 A2 // data pin to the first lca
#define DOUT3 A3 // data pin to the first lca
#define DOUT2 A4 // data pin to the second lca
HX711 scale1;
HX711 scale2;
HX711 scale3;
HX711 scale4;
 
float weight1; 
float weight2;
float weight3;
float weight4;
float calibration_factor = 410640; // for me this value works just perfect 419640 
void setup() {
  scale1.begin(A1, A0);
  scale2.begin(A2, A0);
  scale3.begin(A3, A0);
  scale4.begin(A4, A0);
  
  Serial.begin(9600); // initialize serial communication
  
//  Serial.println("HX711 calibration sketch");
//  Serial.println("Remove all weight from scale");
//  Serial.println("After readings begin, place known weight on scale");
//  Serial.println("Press + or a to increase calibration factor");
//  Serial.println("Press - or z to decrease calibration factor");
  scale1.set_scale();
  scale2.set_scale();
  scale3.set_scale();
  scale4.set_scale();

  scale1.tare(); //Reset the scale to 0
  scale2.tare(); //Reset the scale to 0
  scale3.tare(); //Reset the scale to 0
  scale4.tare(); //Reset the scale to 0
  long zero_factor1 = scale1.read_average(); //Get a baseline reading
  long zero_factor2 = scale2.read_average(); //Get a baseline reading
  long zero_factor3 = scale3.read_average(); //Get a baseline reading
  long zero_factor4 = scale4.read_average(); //Get a baseline reading
//  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
//  Serial.println(zero_factor1);
//  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
//  Serial.println(zero_factor2);
//  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
//  Serial.println(zero_factor3);
//  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
//  Serial.println(zero_factor4);


}
void loop() {
  scale1.set_scale(calibration_factor); //Adjust to this calibration factor
  
  weight1 = scale1.get_units(5); 
  //Serial.print(scale.get_units(), 2);
 // Serial.print(" lbs"); //Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person
 
  scale2.set_scale(calibration_factor); //Adjust to this calibration factor
  
  weight2 = scale2.get_units(5); 
  //Serial.print(scale.get_units(), 2);
 // Serial.print(" lbs"); //Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person
 
  scale3.set_scale(calibration_factor); //Adjust to this calibration factor
  
  weight3 = scale3.get_units(5); 
  //Serial.print(scale.get_units(), 2);
 // Serial.print(" lbs"); //Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person

  scale4.set_scale(calibration_factor); //Adjust to this calibration factor
  //Serial.print("Reading: ");
  weight4  = scale4.get_units(5); 
  //Seria pl.print(scale.get_units(), 2);
 // Serial.print(" lbs"); //Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person
 
  //Serial.print("Kilogram:");
  
  Serial.print( abs(weight1)); 
  Serial.print("Kg ");
  Serial.print( abs(weight2)); 
  Serial.print("Kg ");
  Serial.print( abs(weight3)); 
  Serial.print("Kg ");
  Serial.print( abs(weight4)); 
  Serial.print("Kg ");
  Serial.print(" calibration_factor: ");
  Serial.print(calibration_factor);
  Serial.println();
  if(Serial.available())

  {
    char temp = Serial.read();
    if(temp == '+' || temp == 'a')
      calibration_factor += 10;
    else if(temp == '-' || temp == 'z')
      calibration_factor -= 10;
  }
  
}
