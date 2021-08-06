{
 "metadata": {
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
   "version": "3.8.5"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python385jvsc74a57bd031f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6",
   "display_name": "Python 3.8.5 64-bit"
  },
  "metadata": {
   "interpreter": {
    "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import time\n",
    "\n",
    "headers = {\n",
    "    'Authorization': 'Bearer 948b6cd86bb29150b3e375f2a03386fc69778ff8',\n",
    "}\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "84.3\n",
      "84.3\n",
      "84.3\n",
      "84.3\n",
      "84.3\n",
      "13 27 7 1\n",
      "-55\n",
      "-55\n",
      "-55\n",
      "-55\n",
      "-55\n",
      "interrupted!\n"
     ]
    }
   ],
   "source": [
    "\n",
    "try:\n",
    "    while True:\n",
    "        response = requests.get('https://api.nrfcloud.com/v1/messages', headers=headers)\n",
    "        time.sleep(1)\n",
    "        print(response.json()['items'][0]['message']['data'])\n",
    "except KeyboardInterrupt:\n",
    "    print('interrupted!')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}