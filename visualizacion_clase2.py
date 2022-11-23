{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5c78edfb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import altair as  alt\n",
    "import pandas as  pd\n",
    "import numpy as np\n",
    "from vega_datasets  import data as vega_data\n",
    "\n",
    "data = vega_data.gapminder()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9efc1384",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "data['cluster'] = data['cluster'].astype('category')\n",
    "codes = [0,1,2,3,4,5]\n",
    "lbls  = [\"Asia\",\"Europa\",\"Africa\",\"America\",\"Asia Oriental\",\"Medio Oriente\"]\n",
    "\n",
    "data[\"cluster\"].replace(codes, lbls,inplace =True)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "21dde122",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 693 entries, 0 to 692\n",
      "Data columns (total 6 columns):\n",
      " #   Column       Non-Null Count  Dtype   \n",
      "---  ------       --------------  -----   \n",
      " 0   year         693 non-null    int64   \n",
      " 1   country      693 non-null    object  \n",
      " 2   cluster      693 non-null    category\n",
      " 3   pop          693 non-null    int64   \n",
      " 4   life_expect  693 non-null    float64 \n",
      " 5   fertility    693 non-null    float64 \n",
      "dtypes: category(1), float64(2), int64(2), object(1)\n",
      "memory usage: 28.1+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "77e9e6f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Africa\n",
      "['Kenya' 'Nigeria' 'Rwanda' 'South Africa'] \n",
      "\n",
      "\n",
      "America\n",
      "['Argentina' 'Aruba' 'Bahamas' 'Barbados' 'Bolivia' 'Brazil' 'Canada'\n",
      " 'Chile' 'Colombia' 'Costa Rica' 'Cuba' 'Dominican Republic' 'Ecuador'\n",
      " 'El Salvador' 'Grenada' 'Haiti' 'Jamaica' 'Mexico' 'Peru' 'United States'\n",
      " 'Venezuela'] \n",
      "\n",
      "\n",
      "Asia\n",
      "['Afghanistan' 'Bangladesh' 'India' 'Pakistan'] \n",
      "\n",
      "\n",
      "Asia Oriental\n",
      "['Australia' 'China' 'Hong Kong' 'Indonesia' 'Japan' 'South Korea'\n",
      " 'North Korea' 'New Zealand' 'Philippines'] \n",
      "\n",
      "\n",
      "Europa\n",
      "['Austria' 'Belgium' 'Croatia' 'Finland' 'France' 'Georgia' 'Germany'\n",
      " 'Greece' 'Iceland' 'Ireland' 'Italy' 'Netherlands' 'Norway' 'Poland'\n",
      " 'Portugal' 'Spain' 'Switzerland' 'Turkey' 'United Kingdom'] \n",
      "\n",
      "\n",
      "Medio Oriente\n",
      "['Egypt' 'Iran' 'Iraq' 'Israel' 'Lebanon' 'Saudi Arabia'] \n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "datagroup = data.groupby(\"cluster\")[[\"cluster\",\"country\"]]\n",
    "for key, item in datagroup:\n",
    "    print(key)\n",
    "    print(datagroup.get_group(key)[\"country\"].unique(),\"\\n\\n\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "8282f7a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>pop</th>\n",
       "      <th>life_expect</th>\n",
       "      <th>fertility</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1955.0</td>\n",
       "      <td>5.386500e+04</td>\n",
       "      <td>23.599000</td>\n",
       "      <td>0.940000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2005.0</td>\n",
       "      <td>1.303182e+09</td>\n",
       "      <td>82.603000</td>\n",
       "      <td>8.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>median</th>\n",
       "      <td>1980.0</td>\n",
       "      <td>1.229200e+07</td>\n",
       "      <td>69.498000</td>\n",
       "      <td>2.930000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>skew</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.477306e+00</td>\n",
       "      <td>-0.960409</td>\n",
       "      <td>0.724386</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          year           pop  life_expect  fertility\n",
       "min     1955.0  5.386500e+04    23.599000   0.940000\n",
       "max     2005.0  1.303182e+09    82.603000   8.500000\n",
       "median  1980.0  1.229200e+07    69.498000   2.930000\n",
       "skew       0.0  5.477306e+00    -0.960409   0.724386"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.agg(\n",
    "{\"year\" : [\"min\", \"max\", \"median\", \"skew\"],\n",
    " \"pop\" : [\"min\", \"max\", \"median\", \"skew\"], \n",
    "  \"life_expect\" : [\"min\", \"max\", \"median\", \"skew\"], \n",
    "   \"fertility\":[\"min\", \"max\", \"median\", \"skew\"]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c389ae46",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "287dcefc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53a7ef38",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
