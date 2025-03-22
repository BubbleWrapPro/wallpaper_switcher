# Discord Wallpaper Bot

Ce bot télécharge les images envoyées dans un canal Discord et les définit comme fond d'écran de votre bureau toutes les 10 minutes. Suivez les étapes ci-dessous pour le configurer et l'utiliser.

---

## **Contenu du dossier**
- `bot.exe` : Le fichier exécutable du bot. Double-cliquez dessus pour lancer le bot.
- `config.json` : Fichier de configuration où vous devez ajouter le token de votre bot Discord.
- `backgrounds/` : Dossier où les images téléchargées seront enregistrées.

---

## **Instructions d'installation**

### 1. **Obtenir un jeton de bot Discord**
   - Rendez-vous sur le [Discord Developer Portal](https://discord.com/developers/applications).
   - Créez une nouvelle application, accédez à l'onglet **Bot**, puis générez un token.

### 2. **Configurer le bot**
   - Ouvrez le fichier `config.json` avec un éditeur de texte (par exemple, Notepad ou Bloc-notes).
   - Remplacez `"YOUR_DISCORD_BOT_TOKEN"` par votre jeton Discord :
     ```json
     {
         "BOT_TOKEN": "VOTRE_JETON_DISCORD"
     }
     ```
---

## **Ajouter le bot à votre serveur Discord**
   - Pour inviter le bot sur votre serveur, rechercher ce lien au format suivant :
     ```
     https://discord.com/oauth2/authorize?client_id=VOTRE_CLIENT_ID&scope=bot&permissions=274877910016
     ```
     Remplacez `VOTRE_CLIENT_ID` par l'ID client du bot (disponible sur le Discord Developer Portal).
   - Sélectionnez le server auquel vous voulez l'ajouter (vous devez avoir les permissions de gestion nécessaires)

---

### 3. **Lancer le bot**
   - Double-cliquez sur `bot.exe` pour démarrer le bot. 
   - **Créé une règle de démarrage de `bot.exe` pour un lancement au démarrage en parallèle de discord**
   - Envoyez des images dans un canal Discord auquel le bot a accès. Les images seront enregistrées dans le dossier `backgrounds/` et une image sera définie comme fond d'écran toutes les 10 minutes.

A noter : Les images présentes dans les 100 derniers messages seront également téléchargées

---


## **Dépannage**
- Si le bot ne démarre pas :
  - Vérifiez que votre fichier `config.json` est correctement configuré.
  - Assurez-vous que le dossier `backgrounds/` existe dans le même répertoire que `bot.exe`.

- Si aucune image n'est utilisée comme fond d'écran :
  - Vérifiez que le bot a bien accès au canal Discord et que des images ont été envoyées.
  - Assurez-vous que le chemin d'accès aux images est correct (Windows nécessite des barres obliques inverses `\` dans les chemins).

- Si vous souhaitez faire une débogage, merci d'envoyer un mail à l'addresse suivante afin de recevoir une version 'console' contenant des logs

---

## **À noter**
- Le bot nécessite une connexion internet pour fonctionner correctement.
- Veillez à ne pas partager votre fichier `config.json` contenant votre jeton Discord, car il permettrait à quelqu’un d’autre d’accéder à votre bot.

---

Si vous rencontrez des problèmes ou avez des questions, n'hésitez pas à demander de l'aide !
