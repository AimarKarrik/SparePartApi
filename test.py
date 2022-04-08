import pandas, os, json

def get_csv_convert_to_dict(csv_file_path,):
    print("csv to json conversion in progress...")

    if (os.path.exists('data/Le.json') == True):
        print("Json already exists")
        

    df = pandas.read_csv(csv_file_path, names=("Id","Serial","Nimi", "L1", "L2", "L3", "L4", "L5", "Sus1", "Sus2", "Tootja", "Hind"), low_memory=False)
    df.fillna({"Id": 0, "Serial": "Teadmata", "Nimi": "Teadmata", "L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0, "Sus1": 0.0, "Sus2": 0.0, "Tootja": "Teadmata", "Hind": 0.0}, inplace = True)
    df.astype({"Id": int, "Serial": str, "Nimi": str, "L1": int, "L2": int, "L3": int, "L4": int, "L5": int, "Sus1": float, "Sus2": float, "Tootja": str, "Hind": float})

    print("Conversion finished.")
    return df.to_dict(orient='records')

csv_file_path = r'data/LE.csv'

all_parts = get_csv_convert_to_dict(csv_file_path)

print(all_parts)
