**Activate the virtual environment**

```
./blockchain-env/Scripts/activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```

**Run the application and API**
Make sure to activate the virtual environemnt

```
python -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```
$env:PEER = 'True'; python -m backend.app
```

**Run the frontend**

In the frontend directory:
```
npm run start
```

**Seed the backend with data**
Make sure to activate the virtual environment.

```
$env:SEED_DATA = 'True'; python -m backend.app
```


Things to improve:
    - synchronization without the root node (currently requires an instance of the node to run on :3000, if a new peer joins, it should request a blockchain from another node)
    - catching up a blockchain that's fallen behind
    - API endpoints that read more information (adjustment to the wallet info endpoint or a way to see balances of other addresses)
    - transaction pool validating transactions (right now it accepts any transaction)
    - application for non-miners (people that invest in the cryptocurrency)
    - frontend functionality and styling