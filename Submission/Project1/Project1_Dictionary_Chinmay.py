# Current car brand in india with models and overview specifications

print('\t\t\t\t*******          Existing Car Brands of India          *******\n') 
print('\t\t\t\t******* Brands with Models and overview specifications *******\n')

Cars = {
        "1. Maruti Suzuki":
        {
                "1. Alto": {'Price':'₹ 3.25 Lakh onwards', 'Mileage':'22.05 to 31.59 km/kg', 'Engine':'796 cc', 'Transmission':'Manual', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'4 & 5 Seater'},
                "2. S-Presso": {'Price':'₹ 3.85 Lakh onwards', 'Mileage':'21.53 to 31.19 km/kg', 'Engine':'998 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'4 & 5 Seater'},
                "3. Eeco": {'Price':'₹ 4.53 Lakh onwards', 'Mileage':'16.11 to 20.88 km/kg', 'Engine':'1196 cc', 'Transmission':'Manual', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'5 & 7 Seater'},        
                "4. Ignis": {'Price':'₹ 5.09 Lakh onwards', 'Mileage':'20.89 kmpl', 'Engine':'1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "5. Celerio": {'Price':'₹ 5.14 Lakh onwards', 'Mileage':'25.17 to 26.23 kmpl', 'Engine':'998 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'5 Seater'},
                "6. Wagon R": {'Price':'₹ 5.16 Lakh onwards', 'Mileage':'20.52 to 32.52 kmpl', 'Engine':'998 to 1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'5 Seater'},
                "7. Wagon R 2022": {'Price':'₹ 5.40 Lakh onwards', 'Mileage':'23.56 to 34.50 kmpl', 'Engine':'998 to 1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'5 Seater'},
                "8. Swift": {'Price':'₹ 5.90 Lakh onwards', 'Mileage':'23.2 to 23.76 kmpl', 'Engine':'1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "9. Dzire": {'Price':'₹ 6.09 Lakh onwards', 'Mileage':'23.26 to 24.12 kmpl', 'Engine':'1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'5 Seater'},
                "10. Baleno": {'Price':'₹ 6.35 Lakh onwards', 'Mileage':'22.35 to 22.94 kmpl', 'Engine':'1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "11. Vitara Brezza": {'Price':'₹ 7.68 Lakh onwards', 'Mileage':'17.03 to 18.76 kmpl', 'Engine':'1462 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "12. Ertiga": {'Price':'₹ 8.11 Lakh onwards', 'Mileage':'17.99 to 26.2 kmpl', 'Engine':'1462 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'7 Seater'},
                "13. S-Cross": {'Price':'₹ 8.61 Lakh onwards', 'Mileage':'18.43 to 18.55 kmpl', 'Engine':'1462 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "14. Ciaz": {'Price':'₹ 8.67 Lakh onwards', 'Mileage':'20.04 to 20.65 kmpl', 'Engine':'1462 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "15. XL6": {'Price':'₹ 10.02 Lakh onwards', 'Mileage':'17.99 to 19.01 kmpl', 'Engine':'1462 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'6 Seater'} 
        },
        "2. Hyundai":
        {
                "1. Santro": {'Price':'₹ 4.86 Lakh onwards', 'Mileage':'20 to 30 km/kg', 'Engine':'1086 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'5 Seater'},
                "2. Grand i10 Nios": {'Price':'₹ 5.30 Lakh onwards', 'Mileage':'20 to 25 kmpl', 'Engine':'998 to 1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol, CNG & Diesel', 'Seating Capacity':'5 Seater'},
                "3. Aura": {'Price':'₹ 6.00 Lakh onwards', 'Mileage':'20 to 28 kmpl', 'Engine':'998 to 1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol, CNG & Diesel', 'Seating Capacity':'5 Seater'},
                "4. i20": {'Price':'₹ 6.98 Lakh onwards', 'Mileage':'19.65 to 25.2 kmpl', 'Engine':'998 to 1493 cc', 'Transmission':'Manual, Clutchless Manual, Automatic (CVT) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "5. Venue": {'Price':'₹ 6.99 Lakh onwards', 'Mileage':'17.52 to 23.4 kmpl', 'Engine':'998 to 1493 cc', 'Transmission':'Manual, Clutchless Manual & Automatic (Dual Clutch)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "6. Verna": {'Price':'₹ 9.32 Lakh onwards', 'Mileage':'17.7 to 25 kmpl', 'Engine':'998 to 1497 cc', 'Transmission':'Manual, Automatic (Torque Converter), Automatic (CVT) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "7. i20 N Line": {'Price':'₹ 9.91 Lakh onwards', 'Mileage':'20.25 kmpl', 'Engine':'998 cc', 'Transmission':'Clutchless Manual & Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "8. Creta": {'Price':'₹ 10.22 Lakh onwards', 'Mileage':'17 to 21 kmpl', 'Engine':'1353 to 1497 cc', 'Transmission':'Manual, Automatic (CVT), Automatic (Torque Converter) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "9. Alcazar": {'Price':'₹ 16.34 Lakh onwards', 'Mileage':'14.2 to 20.4 kmpl', 'Engine':'1493 to 1999 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'6 & 7 Seater'},
                "10. Elantra": {'Price':'₹ 17.86 Lakh onwards', 'Mileage':'15 to 17.32 kmpl', 'Engine':'1493 to 1999 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "11. Tuscon": {'Price':'₹ 20.69 Lakh onwards', 'Mileage':'13 to 17 kmpl', 'Engine':'1995 to 1999 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "12. Kona Electric": {'Price':'₹ 23.79 Lakh onwards', 'Mileage':'452 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},
        },
        "3. Tata Motors":
        {
                "1. Tiago": {'Price':'₹ 5.22 Lakh onwards', 'Mileage':'19.8 to 23.84 kmpl', 'Engine':'1199 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & CNG ', 'Seating Capacity':'5 Seater'},
                "2. Punch": {'Price':'₹ 5.68 Lakh onwards', 'Mileage':'18.82 to 18.97 kmpl', 'Engine':'1199 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. Tigor": {'Price':'₹ 5.82 Lakh onwards', 'Mileage':'20.3 kmpl', 'Engine':'1199 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & CNG', 'Seating Capacity':'5 Seater'},
                "4. Altroz": {'Price':'₹ 5.99 Lakh onwards', 'Mileage':'19.05 to 25.11 kmpl', 'Engine':'1199 to 1497 cc', 'Transmission':'Manual & Automatic (Dual Clutch)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "5. Tiago NRG": {'Price':'₹ 6.66 Lakh onwards', 'Mileage':'20.09 kmpl', 'Engine':'1199 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "6. Nexon": {'Price':'₹ 7.42 Lakh onwards', 'Mileage':'16 to 22.4 kmpl', 'Engine':'1199 to 1497 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "7. Tigor EV": {'Price':'₹ 12.24 Lakh onwards', 'Mileage':'306 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},
                "8. Harrier": {'Price':'₹ 14.52 Lakh onwards', 'Mileage':'14.63 to 16.35 kmpl', 'Engine':'1956 cc', 'Transmission':'Manual & Automatic (Torque Connverter)', 'Fuel Type':'Diesel', 'Seating Capacity':'5 Seater'},
                "9. Nexon EV": {'Price':'₹ 14.54 Lakh onwards', 'Mileage':'312 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},
                "10. Safari": {'Price':'₹ 15.02 Lakh onwards', 'Mileage':'14.08 to 16.14 kmpl', 'Engine':'1956 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Diesel', 'Seating Capacity':'6 & 7 Seater'},
        },
        "4. Mahindra":
        {
                "1. KUV100 NXT": {'Price':'₹ 6.19 Lakh onwards', 'Mileage':'18 kmpl', 'Engine':'1198 cc', 'Transmission':'Manual', 'Fuel Type':'Petrol', 'Seating Capacity':'6 Seater'},
                "2. XUV300": {'Price':'₹ 8.16 Lakh onwards', 'Mileage':'17 to 20 kmpl', 'Engine':'1197 to 1497 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "3. Bolero": {'Price':'₹ 8.99 Lakh onwards', 'Mileage':'16.7 kmpl', 'Engine':'1493 cc', 'Transmission':'Manual', 'Fuel Type':'Diesel', 'Seating Capacity':'7 Seater'},
                "4. Bolero Neo": {'Price':'₹ 9.00 Lakh onwards', 'Mileage':'17.29 kmpl', 'Engine':'1493 cc', 'Transmission':'Manual', 'Fuel Type':'Diesel', 'Seating Capacity':'7 Seater'},
                "5. Marazzo": {'Price':'₹ 12.79 Lakh onwards', 'Mileage':'17.93 kmpl', 'Engine':'1497 cc', 'Transmission':'Manual', 'Fuel Type':'Diesel', 'Seating Capacity':'7 & 8 Seater'},
                "6. XUV700": {'Price':'₹ 12.96 Lakh onwards', 'Mileage':'16.5 to 19 kmpl', 'Engine':'1997 to 2184 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 & 7 Seater'},
                "7. Thar": {'Price':'₹ 13.17 Lakh onwards', 'Mileage':'15.2 kmpl', 'Engine':'1997 to 2184 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'4 Seater'},
                "8. Scorpio": {'Price':'₹ 13.19 Lakh onwards', 'Mileage':'15 kmpl', 'Engine':'2179 cc', 'Transmission':'Manual', 'Fuel Type':'Diesel', 'Seating Capacity':'7 Seater'},
                "9. Aulturas G4": {'Price':'₹ 28.85 Lakh onwards', 'Mileage':'12.03 kmpl', 'Engine':'2157 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Diesel', 'Seating Capacity':'7 Seater'},
        },
        "5. Kia":
        {
                "1. Sonet": {'Price':'₹ 6.95 Lakh onwards', 'Mileage':'18.2 to 24.1 kmpl', 'Engine':'998 to 1493 cc', 'Transmission':'Manual, Clutchless Manual, Automatic (Dual Clutch) & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "2. Carens": {'Price':'₹ 8.99 Lakh onwards', 'Mileage':'15.7 to 21.3 kmpl', 'Engine':'1353 to 1497 cc', 'Transmission':'Manual, Automatic (Dual Clutch) & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'6 & 7 Seater'},
                "3. Seltos": {'Price':'₹ 9.95 Lakh onwards', 'Mileage':'16.1 to 20.83 kmpl', 'Engine':'1353 to 1497 cc', 'Transmission':'Manual, Clutchless Manual, Automatic (Dual Clutch), Automatic (CVT) & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "4. Carnival": {'Price':'₹ 25.48 Lakh onwards', 'Mileage':'14 kmpl', 'Engine':'2199 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Diesel', 'Seating Capacity':'6 & 7 Seater'},
        },
        "6. Toyota":
        {
                "1. Glanza": {'Price':'₹ 6.39 Lakh onwards', 'Mileage':'22.35 to 22.94 kmpl', 'Engine':'1197 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "2. Urban Cruiser": {'Price':'₹ 8.87 Lakh onwards', 'Mileage':'17.03 to 18.76 kmpl', 'Engine':'1462 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. Innova Crysta": {'Price':'₹ 17.30 Lakh onwards', 'Mileage':'10.2 to 15.6 kmpl', 'Engine':'2393 to 2694 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'7 & 8 Seater'},
                "4. Fortuner": {'Price':'₹ 31.38 Lakh onwards', 'Mileage':'10 to 14.4 kmpl', 'Engine':'2694 to 2755 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'7 Seater'},
                "5. Camry": {'Price':'₹ 41.70 Lakh onwards', 'Mileage':'23 kmpl', 'Engine':'2487 cc', 'Transmission':'Automatic (CVT)', 'Fuel Type':'Hybrid (Petrol + Electric)', 'Seating Capacity':'5 Seater'},
                "6. Vellfire": {'Price':'₹ 89.85 Lakh onwards', 'Mileage':'16.35 kmpl', 'Engine':'2494 cc', 'Transmission':'Automatic (CVT)', 'Fuel Type':'Hybrid (Petrol + Electric)', 'Seating Capacity':'7 Seater'},
        },
        "7. Skoda":
        {
                "1. Slavia": {'Price':'₹ 10.69 Lakh onwards', 'Mileage':'18.07 to 19.47 kmpl', 'Engine':'999 to 1498 cc', 'Transmission':'Manual, Automatic (Torque Converter) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "2. Kushaq": {'Price':'₹ 10.98 Lakh onwards', 'Mileage':'15.78 to 17.88 kmpl', 'Engine':'999 to 1498 cc', 'Transmission':'Manual, Automatic (Torque Converter) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. Octavia": {'Price':'₹ 26.29 Lakh onwards', 'Mileage':'16 kmpl', 'Engine':'1984 cc', 'Transmission':'Automatic (DSG)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "4. Superb": {'Price':'₹ 32.85 Lakh onwards', 'Mileage':'15 kmpl', 'Engine':'1984 cc', 'Transmission':'Automatic (DSG)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "5. Kodiaq": {'Price':'₹ 34.99 Lakh onwards', 'Mileage':'13 kmpl', 'Engine':'1984 cc', 'Transmission':'Automatic (DSG)', 'Fuel Type':'Petrol', 'Seating Capacity':'7 Seater'},
        },
        "8. Volkswagen":
        {
                "1. Polo": {'Price':'₹ 6.49 Lakh onwards', 'Mileage':'16.47 to 17.99 kmpl', 'Engine':'999 cc', 'Transmission':'Manual & Automatic (Toraue Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "2. Vento": {'Price':'₹ 10.00 Lakh onwards', 'Mileage':'16.35 to 17.69 kmpl', 'Engine':'999 cc', 'Transmission':'Manual & Automatic', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. Taigun": {'Price':'₹ 11.00 Lakh onwards', 'Mileage':'16.44 to 18.47 kmpl', 'Engine':'999 to 1498 cc', 'Transmission':'Manual, Automatic (Torque Converter) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "4. Tiguan": {'Price':'₹ 31.99 Lakh onwards', 'Mileage':'17.01 kmpl', 'Engine':'1984 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
        },
        "9. Mercedes-Benz":
        {
                "1. A-Class Limousine": {'Price':'₹ 41.55 Lakh onwards', 'Mileage':'15.5 to 20.0 kmpl', 'Engine':'1332 to 1950 cc', 'Transmission':'Automatic (Torque Converter) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "2. GLA": {'Price':'₹ 45.56 Lakh onwards', 'Mileage':'13.7 to 17.9 kmpl', 'Engine':'1332 to 1950 cc', 'Transmission':'Automatic (Torque Converter) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "3. C-Class": {'Price':'₹ 49.99 Lakh onwards', 'Mileage':'9.6 to 12.6 kmpl', 'Engine':'1950 to 1991 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "4. AMG A34": {'Price':'₹ 57.49 Lakh onwards', 'Mileage':'13.39 kmpl', 'Engine':'1991 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "5. AMG GLA35": {'Price':'₹ 58.70 Lakh onwards', 'Mileage':'13.47 kmpl', 'Engine':'1991 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "6. GLC": {'Price':'₹ 60.99 Lakh onwards', 'Mileage':'12.70 to 17 kmpl', 'Engine':'1950 to 1991 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "7. E-Class": {'Price':'₹ 65.70 Lakh onwards', 'Mileage':'15.0 to 18.0 kmpl', 'Engine':'1950 to 2925 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "8. GLC Coupe": {'Price':'₹ 70.95 Lakh onwards', 'Mileage':'12.74 to 16.34 kmpl', 'Engine':'1950 to 1991 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "9. V-Class": {'Price':'₹ 71.10 Lakh onwards', 'Mileage':'16.34 to 16.67 kmpl', 'Engine':'1950 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Diesel', 'Seating Capacity':'7 Seater'},
                "10. C-Class Cabriolet": {'Price':'₹ 72.35 Lakh onwards', 'Mileage':'13.0 kmpl', 'Engine':'1991 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "11. AMG A45 S": {'Price':'₹ 79.50 Lakh onwards', 'Mileage':'12.05 kmpl', 'Engine':'1991 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "12. C-Coupe": {'Price':'₹ 82.43 Lakh onwards', 'Mileage':'10.87 kmpl', 'Engine':'2996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "13. GLE": {'Price':'₹ 84.18 Lakh onwards', 'Mileage':'11.11 to 14.07 kmpl', 'Engine':'1950 to 2999 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "14. AMG GLC43 Coupe": {'Price':'₹ 85.37 Lakh onwards', 'Mileage':'9.5 kmpl', 'Engine':'2996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "15. EQC": {'Price':'₹ 99.57 Lakh onwards', 'Mileage':'361 to 420 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},
                "16. AMG E53": {'Price':'₹ 1.04 Crore onwards', 'Mileage':'11.76 kmpl', 'Engine':'2999 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "17. GLS": {'Price':'₹ 1.14 Crore onwards', 'Mileage':'10.1 to 12.5 kmpl', 'Engine':'2925 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'7 Seater'},
                "18. AMG GLE Coupe": {'Price':'₹ 1.56 Crore onwards', 'Mileage':'8.26 to 9.52 kmpl', 'Engine':'2999 to 3892 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "19. S-Class": {'Price':'₹ 1.59 Crore onwards', 'Mileage':'10.1 to 13.5 kmpl', 'Engine':'2925 to 2999 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "20. G-Class": {'Price':'₹ 1.64 Crore onwards', 'Mileage':'6.1 to 9.35 kmpl', 'Engine':'2925 to 3982 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "21. AMG E63": {'Price':'₹ 1.74 Crore onwards', 'Mileage':'8.62 kmpl', 'Engine':'3982 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "22. S-Class (W222)": {'Price':'₹ 2.29 Crore onwards', 'Mileage':'7.09 to 9.8 kmpl', 'Engine':'3982 to 5980 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "23. Maybach GLS": {'Price':'₹ 2.47 Crore onwards', 'Mileage':'8.5 kmpl', 'Engine':'3982 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "24. AMG GT 4-Door Coupe": {'Price':'₹ 2.60 Crore onwards', 'Mileage':'8.85 kmpl', 'Engine':'3982 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "25. AMG GT": {'Price':'₹ 2.64 Crore onwards', 'Mileage':'8.06 kmpl', 'Engine':'3982 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},
        },
        "10. Honda":
        {
                "1. Amaze": {'Price':'₹ 6.41 Lakh onwards', 'Mileage':'18.3 to 24.7 kmpl', 'Engine':'1199 to 1498 cc', 'Transmission':'Manual & Automatic (CVT)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "2. Jazz": {'Price':'₹ 7.81 Lakh onwards', 'Mileage':'16.6 to 17.1 kmpl', 'Engine':'1199 cc', 'Transmission':'Manual & Automatic (CVT)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. WR-V": {'Price':'₹ 8.97 Lakh onwards', 'Mileage':'16.5 to 23.7 kmpl', 'Engine':'1199 to 1498 cc', 'Transmission':'Manual', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "4. City": {'Price':'₹ 9.33 Lakh onwards', 'Mileage':'17.4 kmpl', 'Engine':'1497 cc', 'Transmission':'Manual', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "5. All New City": {'Price':'₹ 11.26 Lakh onwards', 'Mileage':'17.8 to 24.1 kmpl', 'Engine':'1498 cc', 'Transmission':'Manual & Automatic (CVT)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
        },
        "11. BMW":
        {
                "1. X1": {'Price':'₹ 39.84 Lakh onwards', 'Mileage':'15.0 to 20.0 kmpl', 'Engine':'1995 to 1998 cc', 'Transmission':'Automatic (Torque Converter) & Automatic (Dual Clutch)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "2. 2 Series Gran Coupe": {'Price':'₹ 39.90 Lakh onwards', 'Mileage':'14.82 to 18.64 kmpl', 'Engine':'1995 to 1998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "3. 3 Series": {'Price':'₹ 45.36 Lakh onwards', 'Mileage':'12.0 to 20.0 kmpl', 'Engine':'1995 to 1998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "4. 3 Series Gran Limousine": {'Price':'₹ 53.00 Lakh onwards', 'Mileage':'15.30 to 19.62 kmpl', 'Engine':'1995 to 1998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "5. X3": {'Price':'₹ 59.90 Lakh onwards', 'Mileage':'13.17 to 16.55 kmpl', 'Engine':'1995 to 1998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "6. 5 Series": {'Price':'₹ 63.90 Lakh onwards', 'Mileage':'14.82 to 20.37 kmpl', 'Engine':'1995 to 2993 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "7. 6 Series GT": {'Price':'₹ 68.50 Lakh onwards', 'Mileage':'13.32 to 18.65 kmpl', 'Engine':'1995 to 2993 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "8. Z4": {'Price':'₹ 69.81 Lakh onwards', 'Mileage':'11.29 to 14.37 kmpl', 'Engine':'1995 to 2998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},
                "9. X4": {'Price':'₹ 70.50 Lakh onwards', 'Mileage':'12.81 to 14.23 kmpl', 'Engine':'1998 to 2993 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "10. X5": {'Price':'₹ 77.90 Lakh onwards', 'Mileage':'11.24 to 13.38 kmpl', 'Engine':'2993 to 2998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "11. M2": {'Price':'₹ 84.37 Lakh onwards', 'Mileage':'10.63 kmpl', 'Engine':'2979 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "12. X6": {'Price':'₹ 1.02 Crore onwards', 'Mileage':'10.31 kmpl', 'Engine':'2998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "13. X7": {'Price':'₹ 1.07 Crore onwards', 'Mileage':'10.54 to 13.38 kmpl', 'Engine':'2993 to 2998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "14. iX": {'Price':'₹ 1.16 Crore onwards', 'Mileage':'452 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},
                "15. 8 Series": {'Price':'₹ 1.31 Crore onwards', 'Mileage':'5.59 to 11.33 kmpl', 'Engine':'2998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "16. 7 Series": {'Price':'₹ 1.42 Crore onwards', 'Mileage':'7.96 to 39.53 kmpl', 'Engine':'2993 to 6952 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol, Diesel & Hybrid(Electric + Petrol)', 'Seating Capacity':'5 Seater'},
                "17. M4 Competition": {'Price':'₹ 1.44 Crore onwards', 'Mileage':'10.8 kmpl', 'Engine':'2993 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "18. M5": {'Price':'₹ 1.69 Crore onwards', 'Mileage':'9.12 kmpl', 'Engine':'4395 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "19. X5 M": {'Price':'₹ 2.03 Crore onwards', 'Mileage':'8.29 kmpl', 'Engine':'4395 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "20. M8": {'Price':'₹ 2.17 Crore onwards', 'Mileage':'6.59 kmpl', 'Engine':'4395 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
        },
        "12. MG":
        {
                "1. Astor": {'Price':'₹ 9.98 Lakh onwards', 'Mileage':'16.8 to 21.4 kmpl', 'Engine':'1349 to 1498 cc', 'Transmission':'Manual, Automatic (Torque Converter) & Automatic (CVT)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "2. Hector": {'Price':'₹ 13.95 Lakh onwards', 'Mileage':'13.96 to 17.41 kmpl', 'Engine':'1451 to 1956 cc', 'Transmission':'Manual, Automatic (Dual Clutch) & Automatic (CVT)', 'Fuel Type':'Petrol, Diesel & Hybrid (Petrol + Electric)', 'Seating Capacity':'5 Seater'},
                "3. Hector Plus": {'Price':'₹ 14.45 Lakh onwards', 'Mileage':'16.6 kmpl', 'Engine':'1451 to 1956 cc', 'Transmission':'Manual & Automatic (Dual Clutch)', 'Fuel Type':'Petrol, Diesel & Hybrid (Petrol + Electric)', 'Seating Capacity':'6 & 7 Seater'},
                "4. Gloster": {'Price':'₹ 30.98 Lakh onwards', 'Mileage':'12.35 kmpl', 'Engine':'1996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Diesel', 'Seating Capacity':'6 & 7 Seater'},
        },
        "13. Audi":
        {
                "1. Q2": {'Price':'₹ 35.00 Lakh onwards', 'Mileage':'6.5 to 15.38 kmpl', 'Engine':'1984 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "2. A4": {'Price':'₹ 39.99 Lakh onwards', 'Mileage':'17.42 kmpl', 'Engine':'1984 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. A6": {'Price':'₹ 58.70 Lakh onwards', 'Mileage':'14.11 to 16.66 kmpl', 'Engine':'1984 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "4. Q5": {'Price':'₹ 59.21 Lakh onwards', 'Mileage':'13.47 kmpl', 'Engine':'1984  cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "5. Q7": {'Price':'₹ 79.99 Lakh onwards', 'Mileage':'11.21 kmpl', 'Engine':'2995 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'7 Seater'},
                "6. S5 Sportback": {'Price':'₹ 82.48 Lakh onwards', 'Mileage':'10.6 kmpl', 'Engine':'2994 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "7. e-tron": {'Price':'₹ 1.01 Crore onwards', 'Mileage':'400 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},
                "8. Q8": {'Price':'₹ 1.01 Crore onwards', 'Mileage':'9.1 to 9.8 kmpl', 'Engine':'2995 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'7 Seater'},
                "9. RS5": {'Price':'₹ 1.07 Crore onwards', 'Mileage':'10.87 kmpl', 'Engine':'2894 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "10. e-tron Sportback": {'Price':'₹ 1.19 Crore onwards', 'Mileage':'400 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},
                "11. A8 L": {'Price':'₹ 1.58 Crore onwards', 'Mileage':'12 kmpl', 'Engine':'2995 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "12. e-tron GT": {'Price':'₹ 1.80 Crore onwards', 'Mileage':'388 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},
                "13. RS Q8": {'Price':'₹ 2.12 Crore onwards', 'Mileage':'8 kmpl', 'Engine':'3996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "14. RS7 Sportback": {'Price':'₹ 2.19 Crore onwards', 'Mileage':'8.7 kmpl', 'Engine':'3996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
        },
        "14. Renault":
        {
                "1. Kwid": {'Price':'₹ 4.49 Lakh onwards', 'Mileage':'20.71 to 22 kmpl', 'Engine':'799 to 999 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "2. Triber": {'Price':'₹ 5.67 Lakh onwards', 'Mileage':'18.29 to 19 kmpl', 'Engine':'999 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'7 Seater'},
                "3. Kiger": {'Price':'₹ 5.79 Lakh onwards', 'Mileage':'19.03 to 20.53 kmpl', 'Engine':'999 cc', 'Transmission':'Manual & AMT & Automatic (CVT)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "4. Duster": {'Price':'₹ 9.85 Lakh onwards', 'Mileage':'14.19 to 16.5 kmpl', 'Engine':'1330 to 1498 cc', 'Transmission':'Manual & Automatic (CVT)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
        },
        "15. Land Rover":
        {
                "1. Discovery Sport": {'Price':'₹ 65.23 Lakh onwards', 'Mileage':'10.53 to 13.17 kmpl', 'Engine':'1997 to 1999 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'7 Seater'},
                "2. Range Rover Evoque": {'Price':'₹ 69.99 Lakh onwards', 'Mileage':'10.99 kmpl', 'Engine':'1997 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. Defender": {'Price':'₹ 80.72 Lakh onwards', 'Mileage':'8.61 to 11.44 kmpl', 'Engine':'1997 to 2996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "4. Range Rover Velar": {'Price':'₹ 86.75 Lakh onwards', 'Mileage':'13.16 to 15.2 kmpl', 'Engine':'1997 to 1998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "5. Discovery": {'Price':'₹ 88.06 Lakh onwards', 'Mileage':'15.8 kmpl', 'Engine':'1997 to 2996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'7 Seater'},
                "6. Range Rover Sport": {'Price':'₹ 91.23 Lakh onwards', 'Mileage':'7.8 to 12.65 kmpl', 'Engine':'1997 to 5000 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "7. Range Rover": {'Price':'₹ 2.11 Crore onwards', 'Mileage':'9.32 to 10.75 kmpl', 'Engine':'2996 to 2997 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 to 7 Seater'},
        },
        "16. Jeep":
        {
                "1. Compass": {'Price':'₹ 17.79 Lakh onwards', 'Mileage':'14.1 to 17.1 kmpl', 'Engine':'1368 to 1956 cc', 'Transmission':'Manual, Automatic (Dual Clutch) & Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},
                "2. Wrangler": {'Price':'₹ 56.33 Lakh onwards', 'Mileage':'12.1 kmpl', 'Engine':'1998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
        },
        "17. Rolls Royce":
        {
                "1. Wraith": {'Price':'₹ 5.00 Crore onwards', 'Mileage':'6.32 kmpl', 'Engine':'6592 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "2. Dawn": {'Price':'₹ 5.92 Crore onwards', 'Mileage':'7.04 kmpl', 'Engine':'6598 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "3. Cullinan": {'Price':'₹ 6.95 Crore onwards', 'Mileage':'6.67 kmpl', 'Engine':'6749 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "4. Phantom VIII": {'Price':'₹ 9.50 Crore onwards', 'Mileage':'7.19 kmpl', 'Engine':'6749 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
        },
        "18. Jaguar":
        {
                "1. XE": {'Price':'₹ 46.64 Lakh onwards', 'Mileage':'13.6 to 13.5 kmpl', 'Engine':'1997 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},  
                "2. XF": {'Price':'₹ 71.60 Lakh onwards', 'Mileage':'13.1 to 19.3 kmpl', 'Engine':'1997 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},   
                "3. F-Pace": {'Price':'₹ 74.54 Lakh onwards', 'Mileage':'12.9 to 19.3 kmpl', 'Engine':'1997 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Diesel', 'Seating Capacity':'5 Seater'},  
                "4. F-Type": {'Price':'₹ 97.93 Lakh onwards', 'Mileage':'9.3 to 12.35 kmpl', 'Engine':'1997 to 5000 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},  
                "5. I-Pace": {'Price':'₹ 1.08 Crore onwards', 'Mileage':'470 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},  
        },
        "19. Nissan":
        {
                "1. Magnite": {'Price':'₹ 5.76 Lakh onwards', 'Mileage':'17.7 to 19.42 kmpl', 'Engine':'999 cc', 'Transmission':'Manual & Automatic (CVT)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "2. Kicks": {'Price':'₹ 9.50 Lakh onwards', 'Mileage':'13.9 to 15.8 kmpl', 'Engine':'1330 to 1498 cc', 'Transmission':'Manual & Automatic (CVT)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. GT-R": {'Price':'₹ 2.12 Crore onwards', 'Mileage':'8.47 kmpl', 'Engine':'3799 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
        },
        "20. Volvo":
        {
                "1. XC40": {'Price':'₹ 43.20 Lakh onwards', 'Mileage':'14.49 kmpl', 'Engine':'1969 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},  
                "2. S60": {'Price':'₹ 45.90 Lakh onwards', 'Mileage':'14.08 kmpl', 'Engine':'1969 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},  
                "3. XC60": {'Price':'₹ 63.50 Lakh onwards', 'Mileage':'12.15 kmpl', 'Engine':'1969 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},  
                "4. S90": {'Price':'₹ 64.90 Lakh onwards', 'Mileage':'16.6 kmpl', 'Engine':'1969 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},  
                "5. XC90": {'Price':'₹ 90.90 Lakh onwards', 'Mileage':'36.0 kmpl', 'Engine':'1969 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Hybrid (Petrol + Electric', 'Seating Capacity':'7 Seater'},  
        },
        "21. Lamborghini":
        {
                "1. Urus": {'Price':'₹ 3.10 Crore onwards', 'Mileage':'7.87 kmpl', 'Engine':'3996 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},  
                "2. Huracan Evo": {'Price':'₹ 3.22 Crore onwards', 'Mileage':'7.28 kmpl', 'Engine':'5204 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},  
                "3. Huracan Evo Spyder": {'Price':'₹ 3.54 Crore onwards', 'Mileage':'7.04 tp 7.19 kmpl', 'Engine':'5204 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},  
                "4. Huracan STO": {'Price':'₹ 4.99 Crore onwards', 'Mileage':'7.19 kmpl', 'Engine':'5204 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},  
        },
        "22. Porsche":
        {
                "1. Macan": {'Price':'₹ 83.21 Lakh onwards', 'Mileage':'12.35 kmpl', 'Engine':'1984 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},  
                "2. 718": {'Price':'₹ 1.22 Crore onwards', 'Mileage':'9.17 to 13.51 kmpl', 'Engine':'1988 to 3995 cc', 'Transmission':'Manual & Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},  
                "3. Cayenne": {'Price':'₹ 1.26 Crore onwards', 'Mileage':'8.77 to 39.32 kmpl', 'Engine':'2995 to 3996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Hybrid (Petrol + Electric)', 'Seating Capacity':'5 Seater'},  
                "4. Cayanne Coupe": {'Price':'₹  Crore onwards', 'Mileage':'8.62 to 41.67 kmpl', 'Engine':'2995 to 3996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Hybrid (Petrol + Electric)', 'Seating Capacity':'4 Seater'},  
                "5. Panamera": {'Price':'₹ 1.45 Crore onwards', 'Mileage':'9.71 to 30.3 kmpl', 'Engine':'1894 to 3996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol & Hybrid (Petrol + Electric)', 'Seating Capacity':'4 Seater'},  
                "6. Taycan": {'Price':'₹ 1.50 Crore onwards', 'Mileage':'354 to 395 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},  
                "7. 911": {'Price':'₹ 1.69 Crore onwards', 'Mileage':'8 to 11.06 kmpl', 'Engine':'2891 to 3996 cc', 'Transmission':'Manual & Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},  
                "8. Taycan Cross Turismo": {'Price':'₹ 1.70 Crore onwards', 'Mileage':'388 to 395 kmpl', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'5 Seater'},  
        },
        "23. Lexus":
        {
                "1. ES": {'Price':'₹ 56.65 Lakh onwards', 'Mileage':'22.58 kmpl', 'Engine':'2487 cc', 'Transmission':'Automatic (CVT)', 'Fuel Type':'Hybrid (Petrol + Electric)', 'Seating Capacity':'5 Seater'},
                "2. NX": {'Price':'₹ 64.90 Lakh onwards', 'Mileage':'17.8 kmpl', 'Engine':'2494 cc', 'Transmission':'Automatic (CVT)', 'Fuel Type':'Hybrid (Petrol + Electric)', 'Seating Capacity':'5 Seater'},
                "3. RX": {'Price':'₹ 1.04 Crore onwards', 'Mileage':'16.55 kmpl', 'Engine':'3456 cc', 'Transmission':'Automatic (CVT)', 'Fuel Type':'Hybrid (Petrol + Electric)', 'Seating Capacity':'7 Seater'},
                "4. LS": {'Price':'₹ 1.91 Crore onwards', 'Mileage':'15.4 kmpl', 'Engine':'3456 cc', 'Transmission':'Automatic (CVT)', 'Fuel Type':'Hybrid (Petrol + Electric)', 'Seating Capacity':'5 Seater'},
                "5. LC": {'Price':'₹ 2.09 Crore onwards', 'Mileage':'14.8 kmpl', 'Engine':'3456 cc', 'Transmission':'Automatic (CVT)', 'Fuel Type':'Hybrid (Petrol + Electric)', 'Seating Capacity':'4 Seater'},
                "6. LX": {'Price':'₹ 2.33 Crore onwards', 'Mileage':'6.9 kmpl', 'Engine':'5663 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'8 Seater'},
        },
        "24. Mini":
        {
                "1. Cooper": {'Price':'₹ 39.00 Lakh onwards', 'Mileage':'16.35 kmpl', 'Engine':'1998 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},       
                "2. Countryman": {'Price':'₹ 41.00 Lakh onwards', 'Mileage':'14.34 kmpl', 'Engine':'1998 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. Cooper Convertible": {'Price':'₹ 45.50 Lakh onwards', 'Mileage':'16.35 kmpl', 'Engine':'1998 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "4. Cooper JCW": {'Price':'₹ 36.50 Lakh onwards', 'Mileage':'17 kmpl', 'Engine':'1998 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "5. Cooper SE": {'Price':'₹ 47.20 Lakh onwards', 'Mileage':'177 km/full charge', 'Engine':'- cc', 'Transmission':'Automatic', 'Fuel Type':'Electric', 'Seating Capacity':'4 Seater'},
        },
        "25. Ferrari":
        {
                "1. Portofino": {'Price':'₹ 3.50 Crore onwards', 'Mileage':'8.85 kmpl', 'Engine':'3855 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "2. Roma": {'Price':'₹ 3.76 Crore onwards', 'Mileage':'8.93 kmpl', 'Engine':'3855 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
                "3. F8 Tributo": {'Price':'₹ 4.02 Crore onwards', 'Mileage':'7.75 kmpl', 'Engine':'3902 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},
                "4. 812 superfast": {'Price':'₹ 5.20 Crore onwards', 'Mileage':'6.2 kmpl', 'Engine':'6496 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},
        },
        "26. Bentley":
        {
                "1. Bentayga": {'Price':'₹ 4.10 Crore onwards', 'Mileage':'7.69 kmpl', 'Engine':'3996 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
        },
        "27. Maserati":
        {
                "1. Ghibli": {'Price':'₹ 1.20 Crore onwards', 'Mileage':'8.00 to 11.49 kmpl', 'Engine':'1998 to 3799 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Hybrid (Petrol + Electric)', 'Seating Capacity':'5 Seater'},
                "2. Levante": {'Price':'₹ 1.45 Crore onwards', 'Mileage':'9.35 to 9.8 kmpl', 'Engine':'2979 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. Quattroporte": {'Price':'₹ 1.80 Crore onwards', 'Mileage':'8.26 to 9.43 kmpl', 'Engine':'2979 to 3799 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "4. MC20": {'Price':'₹ 3.65 Crore onwards', 'Mileage':'8.62 kmpl', 'Engine':'3000 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},
        },
        "28. Citreon":
        {
                "1. C5 Aircross": {'Price':'₹ 32.24 Lakh onwards', 'Mileage':'18.6 kmpl', 'Engine':'1997 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Diesel', 'Seating Capacity':'5 Seater'},
        },
        "29. Isuzu":
        {
                "1. D-Max": {'Price':'₹ 19.03 Lakh onwards', 'Mileage':'12.4 to 16.56 kmpl', 'Engine':'1898 cc', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Diesel', 'Seating Capacity':'5 Seater'},
                "2. MU-X": {'Price':'₹ 33.32 Lakh onwards', 'Mileage':'12.31 to 13.00 kmpl', 'Engine':'1898 cc', 'Transmission':'Automatic (Torque Converter)', 'Fuel Type':'Diesel', 'Seating Capacity':'7 Seater'},
        },
        "30. McLaren":
        {
                "1. GT": {'Price':'₹ 3.72 Crore onwards', 'Mileage':'7 kmpl', 'Engine':'3994 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},
                "2. 720s": {'Price':'₹ 4.65 Crore onwards', 'Mileage':'8.5 kmpl', 'Engine':'3994 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},
        },
        "31. Datsun":
        {
                "1. redi-GO": {'Price':'₹ 3.98 Lakh onwards', 'Mileage':'20.71 to 22.00 kmpl', 'Engine':'799 to 999 cc', 'Transmission':'Manual & AMT', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "2. GO": {'Price':'₹ 4.03 Lakh onwards', 'Mileage':'19.02 to 19.59 kmpl', 'Engine':'1198', 'Transmission':'Manual & Automatic (Torque Converter)', 'Fuel Type':'Petrol', 'Seating Capacity':'5 Seater'},
                "3. GO+": {'Price':'₹ 4.26 Lakh onwards', 'Mileage':'18.57 to 19.02 kmpl', 'Engine':'1198 cc', 'Transmission':'Manual & Automatic (CVT)', 'Fuel Type':'Petrol', 'Seating Capacity':'7 Seater'},
        },
        "32. Force":
        {
                "1. Gurkha": {'Price':'₹ 14.10 Lakh onwards', 'Mileage':'17 kmpl', 'Engine':'2596 cc', 'Transmission':'Manual', 'Fuel Type':'Diesel', 'Seating Capacity':'4 Seater'},
        },
        "33. Aston Martin":
        {
                "1. Vantage": {'Price':'₹ 2.95 Crore onwards', 'Mileage':'8.62 kmpl', 'Engine':'3982 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'2 Seater'},
                "2. DB11": {'Price':'₹ 3.29 Crore onwards', 'Mileage':'8.9 kmpl', 'Engine':'5198 cc', 'Transmission':'Automatic (Dual Clutch)', 'Fuel Type':'Petrol', 'Seating Capacity':'4 Seater'},
        },
}
