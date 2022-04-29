from Project1_Dictionary_Chinmay import Cars
c=1

while c==1:
        for key in Cars:
                print(key)
        search1 = int(input("\nEnter the number for your desired car brand: "))
        print('\n')
        if search1==1:
                for key in Cars['1. Maruti Suzuki']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['1. Maruti Suzuki']['1. Alto']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['1. Alto'][i])
                elif(search2==2):
                        for i in Cars['1. Maruti Suzuki']['2. S-Presso']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['2. S-Presso'][i])
                elif(search2==3):
                        for i in Cars['1. Maruti Suzuki']['3. Eeco']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['3. Eeco'][i])
                elif(search2==4):
                        for i in Cars['1. Maruti Suzuki']['4. Ignis']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['4. Ignis'][i])
                elif(search2==5):
                        for i in Cars['1. Maruti Suzuki']['5. Celerio']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['5. Celerio'][i])
                elif(search2==6):
                        for i in Cars['1. Maruti Suzuki']['6. Wagon R']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['6. Wagon R'][i])
                elif(search2==7):
                        for i in Cars['1. Maruti Suzuki']['7. Wagon R 2022']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['7. Wagon R 2022'][i])
                elif(search2==8):
                        for i in Cars['1. Maruti Suzuki']['8. Swift']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['8. Swift'][i])
                elif(search2==9):
                        for i in Cars['1. Maruti Suzuki']['9. Dzire']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['9. Dzire'][i])
                elif(search2==10):
                        for i in Cars['1. Maruti Suzuki']['10. Baleno']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['10. Baleno'][i])
                elif(search2==11):
                        for i in Cars['1. Maruti Suzuki']['11. Vitara Brezza']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['11. Vitara Brezza'][i])
                elif(search2==12):
                        for i in Cars['1. Maruti Suzuki']['12. Ertiga']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['12. Ertiga'][i])
                elif(search2==13):
                        for i in Cars['1. Maruti Suzuki']['13. S-Cross']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['13. S-Cross'][i])
                elif(search2==14):
                        for i in Cars['1. Maruti Suzuki']['14. Ciaz']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['14. Ciaz'][i])
                elif(search2==15):
                        for i in Cars['1. Maruti Suzuki']['15. XL6']:
                                print(i,'-',  Cars['1. Maruti Suzuki']['15. XL6'][i])
                else:
                        print("Wrong Input")
        elif search1==2:
                for key in Cars['2. Hyundai']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['2. Hyundai']['1. Santro']:
                                print(i,'-',  Cars['2. Hyundai']['1. Santro'][i])
                elif(search2==2):
                        for i in Cars['2. Hyundai']['2. Grand i10 Nios']:
                                print(i,'-',  Cars['2. Hyundai']['2. Grand i10 Nios'][i])
                elif(search2==3):
                        for i in Cars['2. Hyundai']['3. Aura']:
                                print(i,'-',  Cars['2. Hyundai']['3. Aura'][i])
                elif(search2==4):
                        for i in Cars['2. Hyundai']['4. i20']:
                                print(i,'-',  Cars['2. Hyundai']['4. i20'][i])
                elif(search2==5):
                        for i in Cars['2. Hyundai']['5. Venue']:
                                print(i,'-',  Cars['2. Hyundai']['5. Venue'][i])
                elif(search2==6):
                        for i in Cars['2. Hyundai']['6. Verna']:
                                print(i,'-',  Cars['2. Hyundai']['6. Verna'][i])
                elif(search2==7):
                        for i in Cars['2. Hyundai']['7. i20 N Line']:
                                print(i,'-',  Cars['2. Hyundai']['7. i20 N Line'][i])
                elif(search2==8):
                        for i in Cars['2. Hyundai']['8. Creta']:
                                print(i,'-',  Cars['2. Hyundai']['8. Creta'][i])
                elif(search2==9):
                        for i in Cars['2. Hyundai']['9. Alcazar']:
                                print(i,'-',  Cars['2. Hyundai']['9. Alcazar'][i])
                elif(search2==10):
                        for i in Cars['2. Hyundai']['10. Elantra']:
                                print(i,'-',  Cars['2. Hyundai']['10. Elantra'][i])
                elif(search2==11):
                        for i in Cars['2. Hyundai']['11. Tuscon']:
                                print(i,'-',  Cars['2. Hyundai']['11. Tuscon'][i])
                elif(search2==12):
                        for i in Cars['2. Hyundai']['12. Kona Electric']:
                                print(i,'-',  Cars['2. Hyundai']['12. Kona Electric'][i])
                else: 
                        print("Wrong Input")
                
        elif search1==3:
                for key in Cars['3. Tata Motors']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['3. Tata Motors']['1. Tiago']:
                                print(i,'-',  Cars['3. Tata Motors']['1. Tiago'][i])
                elif(search2==2):
                        for i in Cars['3. Tata Motors']['2. Punch']:
                                print(i,'-',  Cars['3. Tata Motors']['2. Punch'][i])
                elif(search2==3):
                        for i in Cars['3. Tata Motors']['3. Tigor']:
                                print(i,'-',  Cars['3. Tata Motors']['3. Tigor'][i])
                elif(search2==4):
                        for i in Cars['3. Tata Motors']['4. Altroz']:
                                print(i,'-',  Cars['3. Tata Motors']['4. Altroz'][i])
                elif(search2==5):
                        for i in Cars['3. Tata Motors']['5. Tiago NRG']:
                                print(i,'-',  Cars['3. Tata Motors']['5. Tiago NRG'][i])
                elif(search2==6):
                        for i in Cars['3. Tata Motors']['6. Nexon']:
                                print(i,'-',  Cars['3. Tata Motors']['6. Nexon'][i])
                elif(search2==7):
                        for i in Cars['3. Tata Motors']['7. Tigor EV']:
                                print(i,'-',  Cars['3. Tata Motors']['7. Tigor EV'][i])
                elif(search2==8):
                        for i in Cars['3. Tata Motors']['8. Harrier']:
                                print(i,'-',  Cars['3. Tata Motors']['8. Harrier'][i])
                elif(search2==9):
                        for i in Cars['3. Tata Motors']['9. Nexon EV']:
                                print(i,'-',  Cars['3. Tata Motors']['9. Nexon EV'][i])
                elif(search2==10):
                        for i in Cars['3. Tata Motors']['10. Safari']:
                                print(i,'-',  Cars['3. Tata Motors']['10. Safari'][i])
                else:
                        print("Wrong Input")   
        elif search1==4:
                for key in Cars['4. Mahindra']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['4. Mahindra']['1. KUV100 NXT']:
                                print(i,'-',  Cars['4. Mahindra']['1. KUV100 NXT'][i])
                elif(search2==2):
                        for i in Cars['4. Mahindra']['2. XUV300']:
                                print(i,'-',  Cars['4. Mahindra']['2. XUV300'][i])
                elif(search2==3):
                        for i in Cars['4. Mahindra']['3. Bolero']:
                                print(i,'-',  Cars['4. Mahindra']['3. Bolero'][i])
                elif(search2==4):
                        for i in Cars['4. Mahindra']['4. Bolero Neo']:
                                print(i,'-',  Cars['4. Mahindra']['4. Bolero Neo'][i])
                elif(search2==5):
                        for i in Cars['4. Mahindra']['5. Marazzo']:
                                print(i,'-',  Cars['4. Mahindra']['5. Marazzo'][i])
                elif(search2==6):
                        for i in Cars['4. Mahindra']['6. XUV700']:
                                print(i,'-',  Cars['4. Mahindra']['6. XUV700'][i])
                elif(search2==7):
                        for i in Cars['4. Mahindra']['7. Thar']:
                                print(i,'-',  Cars['4. Mahindra']['7. Thar'][i])
                elif(search2==8):
                        for i in Cars['4. Mahindra']['8. Scorpio']:
                                print(i,'-',  Cars['4. Mahindra']['8. Scorpio'][i])
                elif(search2==9):
                        for i in Cars['4. Mahindra']['9. Aulturas G4']:
                                print(i,'-',  Cars['4. Mahindra']['9. Aulturas G4'][i])
                else:
                        print("Wrong Input")
        elif search1==5:
                for key in Cars['5. Kia']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['5. Kia']['1. Sonet']:
                                print(i,'-',  Cars['5. Kia']['1. Sonet'][i])
                elif(search2==2):
                        for i in Cars['5. Kia']['2. Carens']:
                                print(i,'-',  Cars['5. Kia']['2. Carens'][i])
                elif(search2==3):
                        for i in Cars['5. Kia']['3. Seltos']:
                                print(i,'-',  Cars['5. Kia']['3. Seltos'][i])
                elif(search2==4):
                        for i in Cars['5. Kia']['4. Carnival']:
                                print(i,'-',  Cars['5. Kia']['4. Carnival'][i])
                else:
                        print("Wrong Input")
        elif search1==6:
                for key in Cars['6. Toyota']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['6. Toyota']['1. Glanza']:
                                print(i,'-',  Cars['6. Toyota']['1. Glanza'][i])
                elif(search2==2):
                        for i in Cars['6. Toyota']['2. Urban Cruiser']:
                                print(i,'-',  Cars['6. Toyota']['2. Urban Cruiser'][i])
                elif(search2==3):
                        for i in Cars['6. Toyota']['3. Innova Crysta']:
                                print(i,'-',  Cars['6. Toyota']['3. Innova Crysta'][i])
                elif(search2==4):
                        for i in Cars['6. Toyota']['4. Fortuner']:
                                print(i,'-',  Cars['6. Toyota']['4. Fortuner'][i])
                elif(search2==5):
                        for i in Cars['6. Toyota']['5. Camry']:
                                print(i,'-',  Cars['6. Toyota']['5. Camry'][i])
                elif(search2==6):
                        for i in Cars['6. Toyota']['6. Vellfire']:
                                print(i,'-',  Cars['6. Toyota']['6. Vellfire'][i])
                else:
                        print("Wrong Input")  
        elif search1==7:
                for key in Cars['7. Skoda']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['7. Skoda']['1. Slavia']:
                                print(i,'-',  Cars['7. Skoda']['1. Slavia'][i])
                elif(search2==2):
                        for i in Cars['7. Skoda']['2. Kushaq']:
                                print(i,'-',  Cars['7. Skoda']['2. Kushaq'][i])
                elif(search2==3):
                        for i in Cars['7. Skoda']['3. Octavia']:
                                print(i,'-',  Cars['7. Skoda']['3. Octavia'][i])
                elif(search2==4):
                        for i in Cars['7. Skoda']['4. Superb']:
                                print(i,'-',  Cars['7. Skoda']['4. Superb'][i])
                elif(search2==5):
                        for i in Cars['7. Skoda']['5. Kodiaq']:
                                print(i,'-',  Cars['7. Skoda']['5. Kodiaq'][i])
                else:
                        print("Wrong Input")
        elif search1==8:
                for key in Cars['8. Volkswagen']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['8. Volkswagen']['1. Polo']:
                                print(i,'-',  Cars['8. Volkswagen']['1. Polo'][i])
                elif(search2==2):
                        for i in Cars['8. Volkswagen']['2. Vento']:
                                print(i,'-',  Cars['8. Volkswagen']['2. Vento'][i])
                elif(search2==3):
                        for i in Cars['8. Volkswagen']['3. Taigun']:
                                print(i,'-',  Cars['8. Volkswagen']['3. Taigun'][i])
                elif(search2==4):
                        for i in Cars['8. Volkswagen']['4. Tiguan']:
                                print(i,'-',  Cars['8. Volkswagen']['4. Tiguan'][i])
                else:
                        print("Wrong Input")
        elif search1==9:
                for key in Cars['9. Mercedes-Benz']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['9. Mercedes-Benz']['1. A-Class Limousine']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['1. A-Class Limousine'][i])
                elif(search2==2):
                        for i in Cars['9. Mercedes-Benz']['2. GLA']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['2. GLA'][i])
                elif(search2==3):
                        for i in Cars['9. Mercedes-Benz']['3. C-Class']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['3. C-Class'][i])
                elif(search2==4):
                        for i in Cars['9. Mercedes-Benz']['4. AMG A34']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['4. AMG A34'][i])
                elif(search2==5):
                        for i in Cars['9. Mercedes-Benz']['5. AMG GLA35']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['5. AMG GLA35'][i])
                elif(search2==6):
                        for i in Cars['9. Mercedes-Benz']['6. GLC']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['6. GLC'][i])
                elif(search2==7):
                        for i in Cars['9. Mercedes-Benz']['7. E-Class']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['7. E-Class'][i])
                elif(search2==8):
                        for i in Cars['9. Mercedes-Benz']['8. GLC Coupe']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['8. GLC Coupe'][i])
                elif(search2==9):
                        for i in Cars['9. Mercedes-Benz']['9. V-Class']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['9. V-Class'][i])
                elif(search2==10):
                        for i in Cars['9. Mercedes-Benz']['10. C-Class Cabriolet']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['10. C-Class Cabriolet'][i])
                elif(search2==11):
                        for i in Cars['9. Mercedes-Benz']['11. AMG A45 S']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['11. AMG A45 S'][i])
                elif(search2==12):
                        for i in Cars['9. Mercedes-Benz']['12. C-Coupe']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['12. C-Coupe'][i])
                elif(search2==13):
                        for i in Cars['9. Mercedes-Benz']['13. GLE']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['13. GLE'][i])
                elif(search2==14):
                        for i in Cars['9. Mercedes-Benz']['14. AMG GLC43 Coupe']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['14. AMG GLC43 Coupe'][i])
                elif(search2==15):
                        for i in Cars['9. Mercedes-Benz']['15. EQC']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['15. EQC'][i])
                elif(search2==16):
                        for i in Cars['9. Mercedes-Benz']['16. AMG E53']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['16. AMG E53'][i])
                elif(search2==17):
                        for i in Cars['9. Mercedes-Benz']['17. GLS']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['17. GLS'][i])
                elif(search2==18):
                        for i in Cars['9. Mercedes-Benz']['18. AMG GLE Coupe']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['18. AMG GLE Coupe'][i])
                elif(search2==19):
                        for i in Cars['9. Mercedes-Benz']['19. S-Class']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['19. S-Class'][i])
                elif(search2==20):
                        for i in Cars['9. Mercedes-Benz']['20. G-Class']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['20. G-Class'][i])
                elif(search2==21):
                        for i in Cars['9. Mercedes-Benz']['21. AMG E63']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['21. AMG E63'][i])
                elif(search2==22):
                        for i in Cars['9. Mercedes-Benz']['22. S-Class (W222)']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['22. S-Class (W222)'][i])
                elif(search2==23):
                        for i in Cars['9. Mercedes-Benz']['23. Maybach GLS']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['23. Maybach GLS'][i])
                elif(search2==24):
                        for i in Cars['9. Mercedes-Benz']['24. AMG GT 4-Door Coupe']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['24. AMG GT 4-Door Coupe'][i])
                elif(search2==25):
                        for i in Cars['9. Mercedes-Benz']['25. AMG GT']:
                                print(i,'-',  Cars['9. Mercedes-Benz']['25. AMG GT'][i])
                else:
                        print("Wrong Input")
        elif search1==10:
                for key in Cars['10. Honda']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['10. Honda']['1. Amaze']:
                                print(i,'-',  Cars['10. Honda']['1. Amaze'][i])
                elif(search2==2):
                        for i in Cars['10. Honda']['2. Jazz']:
                                print(i,'-',  Cars['10. Honda']['2. Jazz'][i])
                elif(search2==3):
                        for i in Cars['10. Honda']['3. WR-V']:
                                print(i,'-',  Cars['10. Honda']['3. WR-V'][i])
                elif(search2==4):
                        for i in Cars['10. Honda']['4. City']:
                                print(i,'-',  Cars['10. Honda']['4. City'][i])
                elif(search2==5):
                        for i in Cars['10. Honda']['5. All New City']:
                                print(i,'-',  Cars['10. Honda']['5. All New City'][i])
                else:
                        print("Wrong Input")
        elif search1==11:
                for key in Cars['11. BMW']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['11. BMW']['1. X1']:
                                print(i,'-',  Cars['11. BMW']['1. X1'][i])
                elif(search2==2):
                        for i in Cars['11. BMW']['2. 2 Series Gran Coupe']:
                                print(i,'-',  Cars['11. BMW']['2. 2 Series Gran Coupe'][i])
                elif(search2==3):
                        for i in Cars['11. BMW']['3. 3 Series']:
                                print(i,'-',  Cars['11. BMW']['3. 3 Series'][i])
                elif(search2==4):
                        for i in Cars['11. BMW']['4. 3 Series Gran Limousine']:
                                print(i,'-',  Cars['11. BMW']['4. 3 Series Gran Limousine'][i])
                elif(search2==5):
                        for i in Cars['11. BMW']['5. X3']:
                                print(i,'-',  Cars['11. BMW']['5. X3'][i])
                elif(search2==6):
                        for i in Cars['11. BMW']['6. 5 Series']:
                                print(i,'-',  Cars['11. BMW']['6. 5 Series'][i])
                elif(search2==7):
                        for i in Cars['11. BMW']['7. 6 Series GT']:
                                print(i,'-',  Cars['11. BMW']['7. 6 Series GT'][i])
                elif(search2==8):
                        for i in Cars['11. BMW']['8. Z4']:
                                print(i,'-',  Cars['11. BMW']['8. Z4'][i])
                elif(search2==9):
                        for i in Cars['11. BMW']['9. X4']:
                                print(i,'-',  Cars['11. BMW']['9. X4'][i])
                elif(search2==10):
                        for i in Cars['11. BMW']['10. X5']:
                                print(i,'-',  Cars['11. BMW']['10. X5'][i])
                elif(search2==11):
                        for i in Cars['11. BMW']['11. M2']:
                                print(i,'-',  Cars['11. BMW']['11. M2'][i])
                elif(search2==12):
                        for i in Cars['11. BMW']['12. X6']:
                                print(i,'-',  Cars['11. BMW']['12. X6'][i])
                elif(search2==13):
                        for i in Cars['11. BMW']['13. X7']:
                                print(i,'-',  Cars['11. BMW']['13. X7'][i])
                elif(search2==14):
                        for i in Cars['11. BMW']['14. iX']:
                                print(i,'-',  Cars['11. BMW']['14. iX'][i])
                elif(search2==15):
                        for i in Cars['11. BMW']['15. 8 Series']:
                                print(i,'-',  Cars['11. BMW']['15. 8 Series'][i])
                elif(search2==16):
                        for i in Cars['11. BMW']['16. 7 Series']:
                                print(i,'-',  Cars['11. BMW']['16. 7 Series'][i])
                elif(search2==17):
                        for i in Cars['11. BMW']['17. M4 Competition']:
                                print(i,'-',  Cars['11. BMW']['17. M4 Competition'][i])
                elif(search2==18):
                        for i in Cars['11. BMW']['18. M5']:
                                print(i,'-',  Cars['11. BMW']['18. M5'][i])
                elif(search2==19):
                        for i in Cars['11. BMW']['19. X5 M']:
                                print(i,'-',  Cars['11. BMW']['19. X5 M'][i])
                elif(search2==20):
                        for i in Cars['11. BMW']['20. M8']:
                                print(i,'-',  Cars['11. BMW']['20. M8'][i])
                else:
                        print("Wrong Input")
        elif search1==12:
                for key in Cars['12. MG']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['12. MG']['1. Astor']:
                                print(i,'-',  Cars['12. MG']['1. Astor'][i])
                elif(search2==2):
                        for i in Cars['12. MG']['2. Hector']:
                                print(i,'-',  Cars['12. MG']['2. Hector'][i])
                elif(search2==3):
                        for i in Cars['12. MG']['3. Hector Plus']:
                                print(i,'-',  Cars['12. MG']['3. Hector Plus'][i])
                elif(search2==4):
                        for i in Cars['12. MG']['4. Gloster']:
                                print(i,'-',  Cars['12. MG']['4. Gloster'][i])
                else:
                        print("Wrong Input")
        elif search1==13:
                for key in Cars['13. Audi']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['13. Audi']['1. Q2']:
                                print(i,'-',  Cars['13. Audi']['1. Q2'][i])
                elif(search2==2):
                        for i in Cars['13. Audi']['2. A4']:
                                print(i,'-',  Cars['13. Audi']['2. A4'][i])
                elif(search2==3):
                        for i in Cars['13. Audi']['3. A6']:
                                print(i,'-',  Cars['13. Audi']['3. A6'][i])
                elif(search2==4):
                        for i in Cars['13. Audi']['4. Q5']:
                                print(i,'-',  Cars['13. Audi']['4. Q5'][i])
                elif(search2==5):
                        for i in Cars['13. Audi']['5. Q7']:
                                print(i,'-',  Cars['13. Audi']['5. Q7'][i])
                elif(search2==6):
                        for i in Cars['13. Audi']['6. S5 Sportback']:
                                print(i,'-',  Cars['13. Audi']['6. S5 Sportback'][i])
                elif(search2==7):
                        for i in Cars['13. Audi']['7. e-tron']:
                                print(i,'-',  Cars['13. Audi']['7. e-tron'][i])
                elif(search2==8):
                        for i in Cars['13. Audi']['8. Q8']:
                                print(i,'-',  Cars['13. Audi']['8. Q8'][i])
                elif(search2==9):
                        for i in Cars['13. Audi']['9. RS5']:
                                print(i,'-',  Cars['13. Audi']['9. RS5'][i])
                elif(search2==10):
                        for i in Cars['13. Audi']['10. e-tron Sportback']:
                                print(i,'-',  Cars['13. Audi']['10. e-tron Sportback'][i])
                elif(search2==11):
                        for i in Cars['13. Audi']['11. A8 L']:
                                print(i,'-',  Cars['13. Audi']['11. A8 L'][i])
                elif(search2==12):
                        for i in Cars['13. Audi']['12. e-tron GT']:
                                print(i,'-',  Cars['13. Audi']['12. e-tron GT'][i])
                elif(search2==13):
                        for i in Cars['13. Audi']['13. RS Q8']:
                                print(i,'-',  Cars['13. Audi']['13. RS Q8'][i])
                elif(search2==14):
                        for i in Cars['13. Audi']['14. RS7 Sportback']:
                                print(i,'-',  Cars['13. Audi']['14. RS7 Sportback'][i])
                else:
                        print("Wrong Input")
        elif search1==14:
                for key in Cars['14. Renault']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['14. Renault']['1. Kwid']:
                                print(i,'-',  Cars['14. Renault']['1. Kwid'][i])
                elif(search2==2):
                        for i in Cars['14. Renault']['2. Triber']:
                                print(i,'-',  Cars['14. Renault']['2. Triber'][i])
                elif(search2==3):
                        for i in Cars['14. Renault']['3. Kiger']:
                                print(i,'-',  Cars['14. Renault']['3. Kiger'][i])
                elif(search2==4):
                        for i in Cars['14. Renault']['4. Duster']:
                                print(i,'-',  Cars['14. Renault']['4. Duster'][i])
                else:
                        print("Wrong Input")
        elif search1==15:
                for key in Cars['15. Land Rover']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['15. Land Rover']['1. Discovery Sport']:
                                print(i,'-',  Cars['15. Land Rover']['1. Discovery Sport'][i])
                elif(search2==2):
                        for i in Cars['15. Land Rover']['2. Range Rover Evoque']:
                                print(i,'-',  Cars['15. Land Rover']['2. Range Rover Evoque'][i])
                elif(search2==3):
                        for i in Cars['15. Land Rover']['3. Defender']:
                                print(i,'-',  Cars['15. Land Rover']['3. Defender'][i])
                elif(search2==4):
                        for i in Cars['15. Land Rover']['4. Range Rover Velar']:
                                print(i,'-',  Cars['15. Land Rover']['4. Range Rover Velar'][i])
                elif(search2==5):
                        for i in Cars['15. Land Rover']['5. Discovery']:
                                print(i,'-',  Cars['15. Land Rover']['5. Discovery'][i])
                elif(search2==6):
                        for i in Cars['15. Land Rover']['6. Range Rover Sport']:
                                print(i,'-',  Cars['15. Land Rover']['6. Range Rover Sport'][i])
                elif(search2==7):
                        for i in Cars['15. Land Rover']['7. Range Rover']:
                                print(i,'-',  Cars['15. Land Rover']['7. Range Rover'][i])
                else:
                        print("Wrong Input")
        elif search1==16:
                for key in Cars['16. Jeep']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['16. Jeep']['1. Compass']:
                                print(i,'-',  Cars['16. Jeep']['1. Compass'][i])
                elif(search2==2):
                        for i in Cars['16. Jeep']['2. Wrangler']:
                                print(i,'-',  Cars['16. Jeep']['2. Wrangler'][i])
                else:
                        print("Wrong Input")
        elif search1==17:
                for key in Cars['17. Rolls Royce']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['17. Rolls Royce']['1. Wraith']:
                                print(i,'-',  Cars['17. Rolls Royce']['1. Wraith'][i])
                elif(search2==2):
                        for i in Cars['17. Rolls Royce']['2. Dawn']:
                                print(i,'-',  Cars['17. Rolls Royce']['2. Dawn'][i])
                elif(search2==3):
                        for i in Cars['17. Rolls Royce']['3. Cullinan']:
                                print(i,'-',  Cars['17. Rolls Royce']['3. Cullinan'][i])
                elif(search2==4):
                        for i in Cars['17. Rolls Royce']['4. Phantom VIII']:
                                print(i,'-',  Cars['17. Rolls Royce']['4. Phantom VIII'][i])
                else:
                        print("Wrong Input")
        elif search1==18:
                for key in Cars['18. Jaguar']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['18. Jaguar']['1. XE']:
                                print(i,'-',  Cars['18. Jaguar']['1. XE'][i])
                elif(search2==2):
                        for i in Cars['18. Jaguar']['2. XF']:
                                print(i,'-',  Cars['18. Jaguar']['2. XF'][i])
                elif(search2==3):
                        for i in Cars['18. Jaguar']['3. F-Pace']:
                                print(i,'-',  Cars['18. Jaguar']['3. F-Pace'][i])
                elif(search2==4):
                        for i in Cars['18. Jaguar']['4. F-Type']:
                                print(i,'-',  Cars['18. Jaguar']['4. F-Type'][i])
                elif(search2==5):
                        for i in Cars['18. Jaguar']['5. I-Pace']:
                                print(i,'-',  Cars['18. Jaguar']['5. I-Pace'][i])
                else:
                        print("Wrong Input")
        elif search1==19:
                for key in Cars['19. Nissan']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['19. Nissan']['1. Magnite']:
                                print(i,'-',  Cars['19. Nissan']['1. Magnite'][i])
                elif(search2==2):
                        for i in Cars['19. Nissan']['2. Kicks']:
                                print(i,'-',  Cars['19. Nissan']['2. Kicks'][i])
                elif(search2==3):
                        for i in Cars['19. Nissan']['3. GT-R']:
                                print(i,'-',  Cars['19. Nissan']['3. GT-R'][i])
                else:
                        print("Wrong Input")
        elif search1==20:
                for key in Cars['20. Volvo']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['20. Volvo']['1. XC40']:
                                print(i,'-',  Cars['20. Volvo']['1. XC40'][i])
                elif(search2==2):
                        for i in Cars['20. Volvo']['2. S60']:
                                print(i,'-',  Cars['20. Volvo']['2. S60'][i])
                elif(search2==3):
                        for i in Cars['20. Volvo']['3. XC60']:
                                print(i,'-',  Cars['20. Volvo']['3. XC60'][i])
                elif(search2==4):
                        for i in Cars['20. Volvo']['4. S90']:
                                print(i,'-',  Cars['20. Volvo']['4. S90'][i])
                elif(search2==5):
                        for i in Cars['20. Volvo']['5. XC90']:
                                print(i,'-',  Cars['20. Volvo']['5. XC90'][i])
                else:
                        print("Wrong Input")
        elif search1==21:
                for key in Cars['21. Lamborghini']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['21. Lamborghini']['1. Urus']:
                                print(i,'-',  Cars['21. Lamborghini']['1. Urus'][i])
                elif(search2==2):
                        for i in Cars['21. Lamborghini']['2. Huracan Evo']:
                                print(i,'-',  Cars['21. Lamborghini']['2. Huracan Evo'][i])
                elif(search2==3):
                        for i in Cars['21. Lamborghini']['3. Huracan Evo Spyder']:
                                print(i,'-',  Cars['21. Lamborghini']['3. Huracan Evo Spyder'][i])
                elif(search2==4):
                        for i in Cars['21. Lamborghini']['4. Huracan STO']:
                                print(i,'-',  Cars['21. Lamborghini']['4. Huracan STO'][i])
                else:
                        print("Wrong Input")
        elif search1==22:
                for key in Cars['22. Porsche']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['22. Porsche']['1. Macan']:
                                print(i,'-',  Cars['22. Porsche']['1. Macan'][i])
                elif(search2==2):
                        for i in Cars['22. Porsche']['2. 718']:
                                print(i,'-',  Cars['22. Porsche']['2. 718'][i])
                elif(search2==3):
                        for i in Cars['22. Porsche']['3. Cayenne']:
                                print(i,'-',  Cars['22. Porsche']['3. Cayenne'][i])
                elif(search2==4):
                        for i in Cars['22. Porsche']['4. Cayanne Coupe']:
                                print(i,'-',  Cars['22. Porsche']['4. Cayanne Coupe'][i])
                elif(search2==5):
                        for i in Cars['22. Porsche']['5. Panamera']:
                                print(i,'-',  Cars['22. Porsche']['5. Panamera'][i])
                elif(search2==6):
                        for i in Cars['22. Porsche']['6. Taycan']:
                                print(i,'-',  Cars['22. Porsche']['6. Taycan'][i])
                elif(search2==7):
                        for i in Cars['22. Porsche']['7. 911']:
                                print(i,'-',  Cars['22. Porsche']['7. 911'][i])
                elif(search2==8):
                        for i in Cars['22. Porsche']['8. Taycan Cross Turismo']:
                                print(i,'-',  Cars['22. Porsche']['8. Taycan Cross Turismo'][i])
                else:
                        print("Wrong Input")
        elif search1==23:
                for key in Cars['23. Lexus']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['23. Lexus']['1. ES']:
                                print(i,'-',  Cars['23. Lexus']['1. ES'][i])
                elif(search2==2):
                        for i in Cars['23. Lexus']['2. NX']:
                                print(i,'-',  Cars['23. Lexus']['2. NX'][i])
                elif(search2==3):
                        for i in Cars['23. Lexus']['3. RX']:
                                print(i,'-',  Cars['23. Lexus']['3. RX'][i])
                elif(search2==4):
                        for i in Cars['23. Lexus']['4. LS']:
                                print(i,'-',  Cars['23. Lexus']['4. LS'][i])
                elif(search2==5):
                        for i in Cars['23. Lexus']['5. LC']:
                                print(i,'-',  Cars['23. Lexus']['5. LC'][i])
                elif(search2==6):
                        for i in Cars['23. Lexus']['6. LX']:
                                print(i,'-',  Cars['23. Lexus']['6. LX'][i])
                else:
                        print("Wrong Input")
        elif search1==24:
                for key in Cars['24. Mini']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['24. Mini']['1. Cooper']:
                                print(i,'-',  Cars['24. Mini']['1. Cooper'][i])
                elif(search2==2):
                        for i in Cars['24. Mini']['2. Countryman']:
                                print(i,'-',  Cars['24. Mini']['2. Countryman'][i])
                elif(search2==3):
                        for i in Cars['24. Mini']['3. Cooper Convertible']:
                                print(i,'-',  Cars['24. Mini']['3. Cooper Convertible'][i])
                elif(search2==4):
                        for i in Cars['24. Mini']['4. Cooper JCW']:
                                print(i,'-',  Cars['24. Mini']['4. Cooper JCW'][i])
                elif(search2==5):
                        for i in Cars['24. Mini']['5. Cooper SE']:
                                print(i,'-',  Cars['24. Mini']['5. Cooper SE'][i])
                else:
                        print("Wrong Input")
        elif search1==25:
                for key in Cars['25. Ferrari']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['25. Ferrari']['1. Portofino']:
                                print(i,'-',  Cars['25. Ferrari']['1. Portofino'][i])
                elif(search2==2):
                        for i in Cars['25. Ferrari']['2. Roma']:
                                print(i,'-',  Cars['25. Ferrari']['2. Roma'][i])
                elif(search2==3):
                        for i in Cars['25. Ferrari']['3. F8 Tributo']:
                                print(i,'-',  Cars['25. Ferrari']['3. F8 Tributo'][i])
                elif(search2==4):
                        for i in Cars['25. Ferrari']['4. 812 superfast']:
                                print(i,'-',  Cars['25. Ferrari']['4. 812 superfast'][i])
                else:
                        print("Wrong Input")
        elif search1==26:
                for key in Cars['26. Bentley']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['26. Bentley']['1. Bentayga']:
                                print(i,'-',  Cars['26. Bentley']['1. Bentayga'][i])
                else:
                        print("Wrong Input")
        elif search1==27:
                for key in Cars['27. Maserati']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['27. Maserati']['1. Ghibli']:
                                print(i,'-',  Cars['27. Maserati']['1. Ghibli'][i])
                elif(search2==2):
                        for i in Cars['27. Maserati']['2. Levante']:
                                print(i,'-',  Cars['27. Maserati']['2. Levante'][i])
                elif(search2==3):
                        for i in Cars['27. Maserati']['3. Quattroporte']:
                                print(i,'-',  Cars['27. Maserati']['3. Quattroporte'][i])
                elif(search2==4):
                        for i in Cars['27. Maserati']['4. MC20']:
                                print(i,'-',  Cars['27. Maserati']['4. MC20'][i])
                else:
                        print("Wrong Input")
        elif search1==28:
                for key in Cars['28. Citreon']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['28. Citreon']['1. C5 Aircross']:
                                print(i,'-',  Cars['28. Citreon']['1. C5 Aircross'][i])
                else:
                        print("Wrong Input")
        elif search1==29:
                for key in Cars['29. Isuzu']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['29. Isuzu']['1. D-Max']:
                                print(i,'-',  Cars['29. Isuzu']['1. D-Max'][i])
                elif(search2==2):
                        for i in Cars['29. Isuzu']['2. MU-X']:
                                print(i,'-',  Cars['29. Isuzu']['2. MU-X'][i])
                else:
                        print("Wrong Input")
        elif search1==30:
                for key in Cars['30. McLaren']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['30. McLaren']['1. GT']:
                                print(i,'-',  Cars['30. McLaren']['1. GT'][i])
                elif(search2==2):
                        for i in Cars['30. McLaren']['2. 720s']:
                                print(i,'-',  Cars['30. McLaren']['2. 720s'][i])
                else:
                        print("Wrong Input")
        elif search1==31:
                for key in Cars['31. Datsun']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['31. Datsun']['1. redi-GO']:
                                print(i,'-',  Cars['31. Datsun']['1. redi-GO'][i])
                elif(search2==2):
                        for i in Cars['31. Datsun']['2. GO']:
                                print(i,'-',  Cars['31. Datsun']['2. GO'][i])
                elif(search2==3):
                        for i in Cars['31. Datsun']['3. GO+']:
                                print(i,'-',  Cars['31. Datsun']['3. GO+'][i])
                else:
                        print("Wrong Input")
        elif search1==32:
                for key in Cars['32. Force']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['32. Force']['1. Gurkha']:
                                print(i,'-',  Cars['32. Force']['1. Gurkha'][i])
                else:
                        print("Wrong Input")
        elif search1==33:
                for key in Cars['33. Aston Martin']:
                        print(key)
                search2 = int(input("\nEnter the number for desired model: "))
                print('\n')
                if(search2==1):
                        for i in Cars['33. Aston Martin']['1. Vantage']:
                                print(i,'-',  Cars['33. Aston Martin']['1. Vantage'][i])
                elif(search2==2):
                        for i in Cars['33. Aston Martin']['2. DB11']:
                                print(i,'-',  Cars['33. Aston Martin']['2. DB11'][i])
                else:
                        print("Wrong Input")
        else:
                print("\nWrong Input")
        
        c = int(input("\n\nPress 1 to Continue\nPress 0 to Exit\nEnter your choice: "))
        print("\n")
        if c==0:
                print("\nThank You!!")        
        elif c!=0 and c!=1: 
                print("Wrong Input.Program Terminating!!")
                