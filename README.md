# Background Switcher Bot

## Description
Ce bot Discord télécharge automatiquement des images envoyées sur un serveur et les utilise pour changer le fond d'écran de l'ordinateur sur lequel il est exécuté. Il est compatible avec Windows et Linux (GNOME).

## Fonctionnalités
- Analyse les messages d'un serveur Discord et télécharge les images jointes.
- Stocke les images dans un dossier local.
- Change automatiquement le fond d'écran à intervalles réguliers.
- Prend en charge la conversion des images au format JPEG.

## Prérequis
- Un serveur Discord avec un bot configuré
- Windows ou Linux (GNOME)
- Créer un fichier token.txt dans le même répertoire
- Créer un dossier vide "backgrounds" dans le même répertoire

## Installation
1. Clonez ce répertoire :
   ```sh
   git clone https://github.com/BubbleWrapDev/Background-Switcher-Bot.git
   cd Background-Switcher-Bot
   ```

2. Récupérez votre token de bot et l'URL du serveur Discord :
   - Créez une application sur [Discord Developer Portal](https://discord.com/developers/applications).
   - Allez dans **Bot**, activez **Privileged Gateway Intents**, et copiez le **Token**.
   - Allez dans **OAuth2 > URL Generator**, cochez `bot`, sélectionnez les permissions nécessaires (ne modifiez pas le **permissions integer**), et copiez l'URL d'invitation.
   - Collez votre **Token** dans un fichier `token.txt`.

3. Exécutez le bot :
   ```sh
   python background_switcher.py
   ```

## Utilisation
- Le bot surveille les messages sur le serveur et télécharge automatiquement les images jointes.
- Il change le fond d'écran à intervalles réguliers (modifiable dans le script).
- Pour Windows, il utilise l'API `ctypes` pour appliquer le fond d'écran.
- Pour Linux (GNOME), il utilise la commande `gsettings`.

## Remarque importante
Vérifiez que le bot dispose des permissions nécessaires sur Discord pour lire l'historique des messages et télécharger les fichiers.

## Avertissement
Ce projet est destiné à un usage personnel. Assurez-vous de respecter les conditions d'utilisation de Discord et de ne pas exposer votre token publiquement.

---
**Auteur :** BubbleWrap (Thomas Heriaud)

